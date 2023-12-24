# Avazu_x2

+ **Dataset description:**

  This dataset contains about 10 days of labeled click-through data on mobile advertisements. It has 22 feature fields including user features and advertisement attributes. Following the same setting in the [AutoGroup](https://dl.acm.org/doi/abs/10.1145/3397271.3401082) work, we randomly split 80% of the data for training and validation, and the remaining 20% for testing, respectively. For all categorical fields, we filter infrequent features by setting the threshold min_category_count=20 and replace them with a default ``<OOV>`` token.

  The dataset statistics are summarized as follows:

  | Dataset  | Total | #Train | #Validation | #Test | 
  | :--------: | :-----: |:-----: | :----------: | :----: | 
  | Avazu_x2 |  40,428,967     | 32,343,173     |      |  8,085,794    | 

+ **Source:** https://www.kaggle.com/c/avazu-ctr-prediction/data
+ **Download:** https://huggingface.co/datasets/reczoo/Avazu_x2/tree/main
+ **RecZoo Datasets:** https://github.com/reczoo/Datasets

+ **Used by papers:** 
    - Bin Liu, Niannan Xue, Huifeng Guo, Ruiming Tang, Stefanos Zafeiriou, Xiuqiang He, Zhenguo Li. [AutoGroup: Automatic Feature Grouping for Modelling Explicit High-Order Feature Interactions in CTR Prediction](https://dl.acm.org/doi/abs/10.1145/3397271.3401082). In SIGIR 2020.

+ **Check the md5sum for data integrity:**
    ```bash
    $ md5sum train.csv test.csv
    c41d786896e2ebe68e08a022199f0ce8  train.csv
    e641ea94c72cdc99b49656d3404f536e  test.csv
    ```
