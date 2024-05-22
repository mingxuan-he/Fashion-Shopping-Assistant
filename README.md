# <p align="center">AI Confident for Amazon Fashion</p>
$${\color{CadetBlue}Mingxuan\space He,\space \color{Maroon}Erika\space Zhang,\space \color{Thistle}Tianze\space Zhang,\space \color{MidnightBlue}Tianfang\space Zhu}$$
<p align="center"><strong>University of Chicago</strong></p> 
<p align="center"><strong>MACS 37000</strong></p> 

Presentation link: [HERE](https://docs.google.com/presentation/d/1ErR92ePgXi02C6yQtHcEhYofE5fTRdAZozAHcLz4fEs/edit?usp=sharing)



## Latest Team Update: Sunday 05/12/24
Meeting Notes [here](https://docs.google.com/document/d/1MtpyfgS40KDQkx7kjWbbZebLXWoS5qvj3-8H67ZHBMM/edit?usp=share_link)

**NEXT MEETING:** Thurs 05/16/24, 11-12:20

**TO DO BEFORE NEXT MEETING**
1. Make multimodal embeddings (Everyone-pick what you're interested in/can do)
   * Text embed
   * Text to Graph embed
   * Image & Text embed
   * Image & Text to Graph embed (extract features from images?)
2. Knowledge graph (Tian)
  * Url: https://workspace-preview.neo4j.io/connection/connect
  * username and password in the shared drive 
3. Play with Neo4j to make queries & test embeddings (Everyone)

**NEW DATA**
1. A [large-scale Amazon Reviews dataset](https://amazon-reviews-2023.github.io) collected in 2023 by the McAuley Lab at UCSD. This dataset contains produdct and review information from 1996-2023. 
2. We will be focusing on the "Amazon_Fashion" category of products
3. The Review and Metadata data files can be merged with a common key called "parent_asin"
4. A sample tabular merged datafile with 1000 items can be found in the "data" folder called [amazon_subset_0512.csv](https://github.com/mingxuan-he/Amazon-KDD/blob/main/data/amazon_subset_0512.csv) 

**Research framing:**

<img width="454" alt="Screenshot 2024-05-12 at 6 19 33 PM" src="https://github.com/mingxuan-he/Amazon-KDD/assets/143452850/01efb021-a697-4d27-83c3-1239e268acbf">


## FINALS details

**PROJECT**
* 3 forms of data in a SINGLE model
* 3 types of models (from 3 separate weeks)
* Validate inferences, predictions, results

**PRESENTATION**
* 8 minutes/32 slides for 4-person team
* Slides due Thursday 5/23 4:00pm
* Ignite style presentation Thursday 5/23, 4:30pm (We should aim to start presentation over the weekend?)

**WRITEUP**
* Due Friday 5/24, 5:00pm
* Medium post: A detailed, entertaining and informative public-facing **Medium.com blog-post** about their projects that includes the motivation, methodological justification and detail, descriptive data and deep learning modeling, interpretation of findings (e.g., discovered structures, predictions, generations), conclusion, and annotated code appendix. These should not read like an academic paper, but a mixture of (1) explanatory tutorial; and (2) digital museum exhibit, balancing intermittent text with figures, description boxes, equations, and/or conceptual diagrams including at least one visual element (e.g., figure, graph, conceptual diagram) for every 300 words of text; and a minimum total of 5000 words and 17 visual elements.


## Resources:
**Amazon Reviews**
- McAuley Lab [Amazon Reviews 2023 dataset](https://amazon-reviews-2023.github.io) 

**Amazon KDD**
- Amazon KDD Cup: https://www.aicrowd.com/challenges/amazon-kdd-cup-2024-multi-task-online-shopping-challenge-for-llms
  - Starter Kit repo: https://gitlab.aicrowd.com/aicrowd/challenges/amazon-kdd-cup-2024/amazon-kdd-cup-2024-starter-kit
  - Development data: https://gitlab.aicrowd.com/aicrowd/challenges/amazon-kdd-cup-2024/amazon-kdd-cup-2024-starter-kit/-/blob/master/data/development.json
- Training data (maybe):
  - Webshop: https://github.com/princeton-nlp/webshop
  - An agent benchmark using Webshop: https://github.com/THUDM/AgentBench
- Langchain: https://python.langchain.com/docs/
- Dataset and Instruction: https://gitlab.aicrowd.com/aicrowd/challenges/amazon-kdd-cup-2024/amazon-kdd-cup-2024-starter-kit/-/tree/master


## FAQ
https://discourse.aicrowd.com/t/where-is-the-shopbench-amazon-dataset/9730


## Team Google Drive
[Link here](https://drive.google.com/drive/folders/18EXfDk-9wlKeEkK208alQxfbmMyE2VH4?usp=share_link)
