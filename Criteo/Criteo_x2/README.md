# Criteo_x2

+ **Dataset description:**

  This dataset employs the [Criteo 1TB Click Logs](https://ailab.criteo.com/criteo-1tb-click-logs-dataset/) for display advertising, which contains one month of click-through data with billions of data samples. Following the same setting with the [AutoGroup](https://dl.acm.org/doi/abs/10.1145/3397271.3401082) work, we select "data 6-12" as the training set while using "day-13" for testing. To reduce label imbalance, we perform negative sub-sampling to keep the positive ratio roughly at 50%. It has 13 numerical feature fields and 26 categorical feature fields. In this setting, 13 numerical fields are converted into categorical values through bucketizing, while categorical features appearing less than 20 times are set as a default ``<OOV>`` feature.

  The dataset statistics are summarized as follows:

  | Dataset Split  | Total | #Train | #Validation | #Test | 
  | :--------: | :-----: |:-----: | :----------: | :----: | 
  | Criteo_x2 |   99,616,043    |  86,883,012    |      |  12,733,031    |   

+ **Source:** https://ailab.criteo.com/criteo-1tb-click-logs-dataset
+ **Download:** https://huggingface.co/datasets/reczoo/Criteo_x2/tree/main
+ **RecZoo Datasets:** https://github.com/reczoo/Datasets

+ **Used by papers:** 
    - Bin Liu, Niannan Xue, Huifeng Guo, Ruiming Tang, Stefanos Zafeiriou, Xiuqiang He, Zhenguo Li. [AutoGroup: Automatic Feature Grouping for Modelling Explicit High-Order Feature Interactions in CTR Prediction](https://dl.acm.org/doi/abs/10.1145/3397271.3401082). In SIGIR 2020.

+ **Check the md5sum for data integrity:**
    ```bash
    $ md5sum train.csv test.csv
    d4d08405e95836ee049455cae0f8b0d6  train.csv
    32c14fbc7bfe02e72b501793e8db660b  test.csv
    ```
