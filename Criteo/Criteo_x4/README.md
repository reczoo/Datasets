# Criteo_x4

+ **Dataset description:**

  The Criteo dataset is a widely-used benchmark dataset for CTR prediction, which contains about one week of click-through data for display advertising. It has 13 numerical feature fields and 26 categorical feature fields. Following the setting with the [AutoInt work](https://arxiv.org/abs/1810.11921), we randomly split the data into 8:1:1 as the training set, validation set, and test set, respectively. 

  The dataset statistics are summarized as follows:

  | Dataset Split  | Total | #Train | #Validation | #Test | 
  | :--------: | :-----: |:-----: | :----------: | :----: | 
  | Criteo_x4 |  45,840,617     |   36,672,493  |   4,584,062    |  4,584,062    |    


  - Criteo_x4_001

    In this setting, we follow the winner's solution of the Criteo challenge to discretize each integer value x to ⌊log2(x)⌋, if x > 2; and x = 1 otherwise. For all categorical fields, we replace infrequent features with a default ``<OOV>`` token by setting the threshold min_category_count=10. Note that we do not follow the exact preprocessing steps in AutoInt, because this preprocessing performs much better. We fix **embedding_dim=16** as with AutoInt.
    
  - Criteo_x4_002

    In this setting, we follow the winner's solution of the Criteo challenge to discretize each integer value x to ⌊log2(x)⌋, if x > 2; and x = 1 otherwise. For all categorical fields, we replace infrequent features with a default ``<OOV>`` token by setting the threshold min_category_count=2. We fix **embedding_dim=40** in this setting.


+ **Source:** https://www.kaggle.com/c/criteo-display-ad-challenge/data
+ **Download:** https://huggingface.co/datasets/reczoo/Criteo_x4/tree/main
+ **RecZoo Datasets:** https://github.com/reczoo/Datasets

+ **Used by papers:** 
  - Weiping Song, Chence Shi, Zhiping Xiao, Zhijian Duan, Yewen Xu, Ming Zhang, Jian Tang. [AutoInt: Automatic Feature Interaction Learning via Self-Attentive Neural Networks](https://arxiv.org/abs/1810.11921). In CIKM 2019.
  - Jieming Zhu, Jinyang Liu, Shuai Yang, Qi Zhang, Xiuqiang He. [BARS-CTR: Open Benchmarking for Click-Through Rate Prediction](https://arxiv.org/abs/2009.05794). In CIKM 2021.

+ **Check the md5sum for data integrity:**
  ```bash
  $ md5sum train.csv valid.csv test.csv
  4a53bb7cbc0e4ee25f9d6a73ed824b1a  train.csv
  fba5428b22895016e790e2dec623cb56  valid.csv
  cfc37da0d75c4d2d8778e76997df2976  test.csv
  ```
