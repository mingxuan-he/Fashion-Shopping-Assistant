import os
from dotenv import load_dotenv
from typing import Any, List, Dict
import base64

from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from langchain.agents import AgentExecutor, create_tool_calling_agent, tool
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


class ProductSearchInput(BaseModel):
    """Input for the search_product tool."""
    query: str = Field(
        description="Query to search in the product database."
    )
    # TODO: add more fields as filters e.g. max_price


class ShoppingAssistant():
    
    def __init__(self, config: Dict=None):
        
        ##### configurations #####
        env = load_dotenv()
        # self.HF_API_KEY = os.getenv("HF_API_KEY")
        if not config:
            # TODO: make sure the query embedding model matches doc embedding model
            config = {
                "clip_model_name": "clip-ViT-B-32",
                "openai_embedding_model_name": "text-embedding-3-large",
                "image_vector_store_name": "clip-embed",
                "text_vector_store_name": "description-embed",
                "image_search_weight": 0.5, # might need some exploration
                "top_k_initial": 10, # probably need to increase this
                "top_k_final": 3
            }
        self.config = config
        
        ###### search_product tool #####
        # pinecone
        self.pinecone = Pinecone()
        self.image_vector_store = self.pinecone.Index(self.config["image_vector_store_name"])
        self.text_vector_store = self.pinecone.Index(self.config["text_vector_store_name"])
        
        print("Pinecone connected")
        
        # initialize embedding models
        self.clip_model = SentenceTransformer(self.config["clip_model_name"])
        self.openai_emb_model = OpenAIEmbeddings(model=self.config["openai_embedding_model_name"])
        
        print("Embedding models loaded")
        
        # search_product tool
        @tool(args_schema=ProductSearchInput)
        def search_product(
                query: str
                # TODO: filter parameters https://docs.pinecone.io/guides/data/filter-with-metadata
            ) -> List[Dict[str, Any]]:
            """search for a product in the database"""
            # compute CLIP embeddings for query (local)
            clip_emb = self.clip_model.encode(
                [query],
                convert_to_tensor=False,
                show_progress_bar=False
            ).tolist()
            
            # compute openai embeddings for query (API)
            text_emb = self.openai_emb_model.embed_query(query)
            
            k_initial = self.config["top_k_initial"]
            
            image_matches = self.image_vector_store.query(
                vector=clip_emb,
                top_k=k_initial,
                include_values=False,
                include_metadata=False
            )["matches"]
            
            text_matches = self.text_vector_store.query(
                vector=text_emb,
                top_k=k_initial,
                include_values=False,
                include_metadata=False
            )["matches"]
            
            # combine scores from image and text search
            agg_scores = self._join_scores(image_matches, text_matches)
            
            print("Image matches:", image_matches)
            print("Text matches:", text_matches)
            print("Aggregated scores:", agg_scores)
            
            # get product data for top k products
            k_final = self.config["top_k_final"]
            sorted_items = sorted(agg_scores.items(), key=lambda x: x[1], reverse=True)
            sorted_ids = [item[0] for item in sorted_items]
            details = self.text_vector_store.fetch(sorted_ids[:k_final])
            
            # return the metadata of the top k products
            product_info = [product["metadata"] for product in details["vectors"].values()]
            return product_info
        
        print("Retriever tool created. Tool info:")
        print(search_product.description)
        print(search_product.args)
        print('\n')
        
        ###### LLM agent ######
        # TODO: better system prompt
        sys_prompt = """
        You are an online shopping assistant. Your job is to help users find products, provide product details, and answer questions.
        Use the search_product tool to find relevant products in the database.
        Markdown is enabled for displaying product images.
        Below is the user's information. Tailor your assistance to best suit their needs.
        **User Information:**
        """
        
        # TODO: pass in user info dynamically
        user_info = """
        Name: James
        Age: Middle-aged
        Gender: Male
        Height: 6'1
        Location: Chicago, IL
        Occupation: Sociology Professor
        """
        
        sys_prompt += user_info

        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=sys_prompt),
                MessagesPlaceholder(variable_name='chat_history'),
                HumanMessagePromptTemplate.from_template("{input}"),
                MessagesPlaceholder(variable_name='agent_scratchpad')
            ]
        )

        llm = ChatOpenAI(model="gpt-4o", temperature=0)

        agent = create_tool_calling_agent(
            llm=llm,
            tools=[search_product], 
            prompt=prompt
        )
        
        self.chat_history = []
        self.agent = AgentExecutor(
            agent=agent, 
            tools=[search_product], 
            verbose=True
        )
    
    
    def _join_scores(self, image_matches, text_matches, image_weight=None):
        # helper func to combine scores from image and text search
        
        if not image_weight:
            image_weight = self.config["image_search_weight"]
        
        agg_scores = {}
        for match in image_matches:
            id = match["id"]
            score = match["score"] * image_weight
            agg_scores[id] = score
            
        for match in text_matches:
            id = match["id"]
            score = match["score"] * (1-image_weight)
            if id in agg_scores:
                agg_scores[id] += score
            else:
                agg_scores[id] = score
        
        return agg_scores
    
    
    ##### public methods #####
    
    def get_history(self):
        return self.chat_history
    

    def chat(self, input_text: str=None, input_image: str=None, image_is_file: bool=False):
        if input_image:
            if image_is_file:
                with open(input_image, "rb") as f:
                    image = base64.b64encode(f.read()).decode("utf-8")
            else: # if base64 image is passed
                image = input_image
            
        # add text and image to human message content
        input_content = []
        if input_text:
            input_content.append({
                "type":"text", 
                "text": input_text
            })
        if input_image:
            input_content.append({
                "type": "image_url", 
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image}"
                    }
            })
        
        # invoke agent
        response = self.agent.invoke({
            "chat_history": self.chat_history,
            "input": input_content
        })
        
        output = response["output"]
        
        # store chat history
        self.chat_history.extend([
            HumanMessage(content=input_content),
            AIMessage(content=output)
        ])
        
        return output
        
        
if __name__ == "__main__":
    assistant = ShoppingAssistant()
    image_path = "data/test_image.jpg"
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    response = assistant.chat(input_text="Describe this item and find me a top that goes well with it.", input_image=encoded, image_is_file=False)
    # response = assistant.chat(input_text="Describe this item and find me a top that goes well with it.", input_image=image_path, image_is_file=True)
    print(response)
    print(assistant.get_history())
