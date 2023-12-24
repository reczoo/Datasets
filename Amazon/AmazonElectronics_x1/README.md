# AmazonElectronics_x1

+ **Dataset description:**

  The [Amazon dataset](http://jmcauley.ucsd.edu/data/amazon) contains product reviews and metadata from Amazon, which is a widely-used benchmark dataset. We use the preprocessed subset named Amazon-Electronics from the [DIN](https://arxiv.org/abs/1706.06978) work. It contains 192,403 users, 63,001 goods, 801 categories and 1,689,188 samples. User behaviors in this dataset are rich, with more than 5 reviews for each user and goods. Features include goods_id, cate_id, user reviewed goods_id_list and cate_id_list. Following DIN, the task is to predict the probability of reviewing the (k+1)-th goods by making use of the first k reviewed goods. The last item of each behavior sequence is reserved for testing.

  The dataset statistics are summarized as follows.

  | Dataset Split  | Total | #Train | #Validation | #Test | 
  | :--------: | :-----: |:-----: | :----------: | :----: | 
  | AmazonElectronics_x1 | 2,993,570   | 2,608,764 |      | 384,806  |

+ **Data format:**
label, user_id, item_id, cate_id, item_history, cate_history

+ **Source:** https://cseweb.ucsd.edu/~jmcauley/datasets.html
+ **Download:** https://huggingface.co/datasets/reczoo/AmazonElectronics_x1/tree/main
+ **RecZoo Datasets:** https://github.com/reczoo/Datasets

+ **Used by papers:**
    - Guorui Zhou, Chengru Song, Xiaoqiang Zhu, Ying Fan, Han Zhu, Xiao Ma, Yanghui Yan, Junqi Jin, Han Li, Kun Gai. [Deep Interest Network for Click-Through Rate Prediction](https://arxiv.org/abs/1706.06978). In KDD 2018.
    - Jieming Zhu, Guohao Cai, Junjie Huang, Zhenhua Dong, Ruiming Tang, Weinan Zhang. [ReLoop2: Building Self-Adaptive Recommendation Models via Responsive Error Compensation Loop](https://arxiv.org/abs/2306.08808). In KDD 2023.

+ **Check the md5sum for data integrity:**
    ```bash
    $ md5sum *.csv
    57a20e82fe736dd495f2eaf0669bf6d0  test.csv
    e9bf80b92985e463db18fdc753d347b5  train.csv
    ```
