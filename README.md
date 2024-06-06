# RecZoo Datasets

+ [CTR Prediction](#ctr-prediction)
+ [Matching](#matching)
+ [Reranking](#reranking)
+ [Multimodal](#multimodal)
+ [Multitask](#multitask)
+ [Multidomain](#multidomain)


## CTR Prediction

| Dataset   | Dataset ID   |   Domain  |  Use Cases   | Download | Leaderboard | 
|:-----------|:--------------------|:------------------------|:-------------------- |:---------------------:|:---------------------:|
| [Criteo](https://github.com/reczoo/Datasets/tree/main/Criteo)    | [Criteo_x1](https://github.com/reczoo/Datasets/tree/main/Criteo/Criteo_x1)              |  Ads | Feature interactions | [:link:](https://huggingface.co/datasets/reczoo/Criteo_x1/resolve/main/Criteo_x1.zip?download=true) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/criteo_x1.html) |
|           | [Criteo_x2](https://github.com/reczoo/Datasets/tree/main/Criteo/Criteo_x2)              |   Ads | Feature interactions | [:link:](https://huggingface.co/datasets/reczoo/Criteo_x2/resolve/main/Criteo_x2.zip?download=true) | 
|           | [Criteo_x4](https://github.com/reczoo/Datasets/tree/main/Criteo/Criteo_x4)              |  Ads |Feature interactions | [:link:](https://huggingface.co/datasets/reczoo/Criteo_x4/resolve/main/Criteo_x4.zip?download=true) |  [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/criteo_x4.html) |
| [Avazu](https://github.com/reczoo/Datasets/tree/main/Avazu)     | [Avazu_x1](https://github.com/reczoo/Datasets/tree/main/Avazu/Avazu_x1)              | Ads |Feature interactions | [:link:](https://huggingface.co/datasets/reczoo/Avazu_x1/resolve/main/Avazu_x1.zip?download=true) |  [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/avazu_x1.html) |
|           | [Avazu_x2](https://github.com/reczoo/Datasets/tree/main/Avazu/Avazu_x2)             | Ads |Feature interactions | [:link:](https://huggingface.co/datasets/reczoo/Avazu_x2/resolve/main/Avazu_x2.zip?download=true) |
|           | [Avazu_x4](https://github.com/reczoo/Datasets/tree/main/Avazu/Avazu_x4)                | Ads |Feature interactions | [:link:](https://huggingface.co/datasets/reczoo/Avazu_x4/resolve/main/Avazu_x4.zip?download=true) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/avazu_x4.html) |
| [KKBox](https://github.com/reczoo/Datasets/tree/main/KKBox)     | [KKBox_x1](https://github.com/reczoo/Datasets/tree/main/KKBox/KKBox_x1)              | Music | Feature interactions | [:link:](https://huggingface.co/datasets/reczoo/KKBox_x1/resolve/main/KKBox_x1.zip?download=true) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/kkbox_x1.html) |
| [Frappe](https://github.com/reczoo/Datasets/tree/main/Frappe)    | [Frappe_x1](https://github.com/reczoo/Datasets/tree/main/Frappe/Frappe_x1)             | Apps | Feature interactions | [:link:](https://huggingface.co/datasets/reczoo/Frappe_x1/resolve/main/Frappe_x1.zip?download=true) |  [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/frappe_x1.html) |
| [MovieLens](https://github.com/reczoo/Datasets/tree/main/MovieLens) | [MovielensLatest_x1](https://github.com/reczoo/Datasets/tree/main/MovieLens/MovielensLatest_x1)   | Movies | Feature interactions | [:link:](https://huggingface.co/datasets/reczoo/MovielensLatest_x1/resolve/main/MovielensLatest_x1.zip?download=true) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/movielenslatest_x1.html) |
| [Taobao](https://github.com/reczoo/Datasets/tree/main/Taobao)    | [TaobaoAd_x1](https://github.com/reczoo/Datasets/tree/main/Taobao/TaobaoAd_x1)              | Ads | Sequence | [:link:](https://huggingface.co/datasets/reczoo/TaobaoAd_x1/resolve/main/TaobaoAd_x1.zip?download=true) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/taobaoad_x1.html) |
| [Amazon](https://github.com/reczoo/Datasets/tree/main/Amazon)            | [AmazonElectronics_x1](https://github.com/reczoo/Datasets/tree/main/Amazon/AmazonElectronics_x1)      | Electronics | Sequence | [:link:](https://huggingface.co/datasets/reczoo/AmazonElectronics_x1/resolve/main/AmazonElectronics_x1.zip?download=true) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/amazonelectronics_x1.html) |
| [iPinYou](https://github.com/reczoo/Datasets/tree/main/iPinYou)        |  [iPinYou_x1](https://github.com/reczoo/Datasets/tree/main/iPinYou/iPinYou_x1)      |    Ads  | Feature interactions | [:link:](https://huggingface.co/datasets/reczoo/iPinYou_x1/resolve/main/iPinYou_x1.zip?download=true) |
| [MicroVideo](https://github.com/reczoo/Datasets/tree/main/MicroVideo)    | [MicroVideo1.7M_x1](https://github.com/reczoo/Datasets/tree/main/MicroVideo/MicroVideo1.7M_x1)               | MicroVideo | Sequence, multimodal | [:link:](https://huggingface.co/datasets/reczoo/MicroVideo1.7M_x1/resolve/main/MicroVideo1.7M_x1.zip?download=true) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/microvideo1.7m_x1.html) |
| [KuaiShou](https://github.com/reczoo/Datasets/tree/main/KuaiShou)        |  [KuaiVideo_x1](https://github.com/reczoo/Datasets/tree/main/KuaiShou/KuaiVideo_x1)      |    MicroVideo  | Sequence, multimodal | [:link:](https://huggingface.co/datasets/reczoo/KuaiVideo_x1/resolve/main/KuaiVideo_x1.zip?download=true) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/kuaivideo_x1.html) |
| [MIND](https://github.com/reczoo/Datasets/tree/main/MIND)  |  [MIND_small_x1](https://github.com/reczoo/Datasets/tree/main/MIND/MIND_small_x1)  |   News  | Sequence, pretraining | [:link:](https://huggingface.co/datasets/reczoo/MIND_small_x1/resolve/main/MIND_small_x1.zip?download=true) | 


## Matching

| Dataset           | Dataset ID           |     Domain  |  Use Cases                        | Download | Leaderboard | 
|:-------------------|:----------------------|:-----------------|:-------------|:----------------------:|:----------------------:|
| [Amazon](https://github.com/reczoo/Datasets/tree/main/Amazon)            | [AmazonBooks_m1](https://github.com/reczoo/Datasets/tree/main/Amazon/AmazonBooks_m1)        | Books | CF, GNN | [:link:](https://huggingface.co/datasets/reczoo/AmazonBooks_m1/tree/main) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/Matching/leaderboard/amazonbooks_m1.html) |
|                   | [AmazonCDs_m1](https://github.com/reczoo/Datasets/tree/main/Amazon/AmazonCDs_m1)         |   CDs | CF, GNN |   [:link:](https://huggingface.co/datasets/reczoo/AmazonCDs_m1/tree/main) |
|                   | [AmazonMovies_m1](https://github.com/reczoo/Datasets/tree/main/Amazon/AmazonMovies_m1)      |   Movies     | CF, GNN | [:link:](https://huggingface.co/datasets/reczoo/AmazonMovies_m1/tree/main) |
|                   | [AmazonBeauty_m1](https://github.com/reczoo/Datasets/tree/main/Amazon/AmazonBeauty_m1)      |   Beauty     | CF, GNN |  [:link:](https://huggingface.co/datasets/reczoo/AmazonBeauty_m1/tree/main) |
|                   | [AmazonElectronics_m1](https://github.com/reczoo/Datasets/tree/main/Amazon/AmazonElectronics_m1) |   Electronics | CF |  [:link:](https://huggingface.co/datasets/reczoo/AmazonElectronics_m1/tree/main) |
| [MovieLens](https://github.com/reczoo/Datasets/tree/main/MovieLens)         | [MovieLens1M_m1](https://github.com/reczoo/Datasets/tree/main/Amazon/MovieLens1M_m1)       |   Movies |    CF, GNN | [:link:](https://huggingface.co/datasets/reczoo/MovieLens1M_m1/tree/main) |
| [Yelp](https://github.com/reczoo/Datasets/tree/main/Yelp)              | [Yelp18_m1](https://github.com/reczoo/Datasets/tree/main/Yelp/Yelp18_m1)            |   Restaurants | CF, GNN | [:link:](https://huggingface.co/datasets/reczoo/Yelp18_m1/tree/main) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/Matching/leaderboard/yelp18_m1.html) |
| [Gowalla](https://github.com/reczoo/Datasets/tree/main/Gowalla)           | [Gowalla_m1](https://github.com/reczoo/Datasets/tree/main/Gowalla/Gowalla_m1)        | POIs | CF, GNN | [:link:](https://huggingface.co/datasets/reczoo/Gowalla_m1/tree/main) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/Matching/leaderboard/gowalla_m1.html) |
| [CiteULike](https://github.com/reczoo/Datasets/tree/main/CiteULike)           | [CiteUlikeA_m1](https://github.com/reczoo/Datasets/tree/main/CiteULike/CiteUlikeA_m1)        | Citation  | CF, GNN | [:link:](https://huggingface.co/datasets/reczoo/CiteUlikeA_m1/tree/main) |


## Reranking
TODO

## Multimodal

| Dataset   | Dataset ID   |   Domain  |  Use Cases   | Download | Leaderboard | 
|:-----------|:--------------------|:------------------------|:-------------------- |:---------------------:|:---------------------:|
| [MicroVideo](https://github.com/reczoo/Datasets/tree/main/MicroVideo)    | [MicroVideo1.7M_x1](https://github.com/reczoo/Datasets/tree/main/MicroVideo/MicroVideo1.7M_x1)               | MicroVideo | Sequence, multimodal | [:link:](https://huggingface.co/datasets/reczoo/MicroVideo1.7M_x1/resolve/main/MicroVideo1.7M_x1.zip?download=true) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/microvideo1.7m_x1.html) |
| [KuaiShou](https://github.com/reczoo/Datasets/tree/main/KuaiShou)        |  [KuaiVideo_x1](https://github.com/reczoo/Datasets/tree/main/KuaiShou/KuaiVideo_x1)      |    MicroVideo  | Sequence, multimodal | [:link:](https://huggingface.co/datasets/reczoo/KuaiVideo_x1/resolve/main/KuaiVideo_x1.zip?download=true) | [:arrow_upper_right:](https://openbenchmark.github.io/BARS/CTR/leaderboard/kuaivideo_x1.html) |


## Multitask
TODO

## Multidomain
TODO

