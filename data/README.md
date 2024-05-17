Update 05/16/24

## **Full merged & clean data files (tabular/dataframes) linked below:**
* [760MB] [amazon_fashion_clean_051624.parquet](https://drive.google.com/file/d/1DePC-rTUNBzQgIqq-GSLA228hNCTxEJL/view?usp=share_link)

FEATURES

* `title` [STR]
* `avg_rating` [FLOAT64]
* `rating_number` [INT64]
* `features` [STR]
* `description` [STR]
* `price` [FLOAT64]
* `images` [LST of DICT]
* `store` [STR]
* `details` [DICT] 
* `parent_asin` [STR]
* `title_review_agg` [STR]
* `user_id` [LST of STR]
* `timestamp` [LST of DATETIME]
* `avg_rating_reviewers` [FLOAT64]
* `coefvar_rating_reviewers` [FLOAT64]
* `text_agg` [STR]
* `text_weighted_agg` [STR]
* `images_review_cln` [LST of DICT]


## **Individual datasets, clean**
* [537MB] [reviews_modified_051624.parquet](https://drive.google.com/file/d/1eFBR7PrBlnVgE6gKwx4J4-dnckiEh8XK/view?usp=share_link)
  * Each row contains one USER and their review. Maybe can be used for graph analysis because of this data format.
* [278MB] [meta_modified_051624.parquet](https://drive.google.com/file/d/131iDXr_TI25X53dG97DGlmz5mvm_eG8k/view?usp=share_link)

## **Raw data**
* Reviews: [Amazon_Fashion.jsonl](https://drive.google.com/file/d/1A_HSH_-vocuNcY4D0AhgTcl-VgspwjCj/view?usp=share_link)
* Product info: [meta_Amazon_Fashion.jsonl](https://drive.google.com/file/d/1fzm243T5JylfFvaqAf5EpBKPmCH5WdX6/view?usp=share_link)

