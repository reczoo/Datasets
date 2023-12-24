# Avazu_x4

+ **Dataset description:**

  This dataset contains about 10 days of labeled click-through data on mobile advertisements. It has 22 feature fields including user features and advertisement attributes. Following the same setting with the [AutoInt](https://arxiv.org/abs/1810.11921) work, we split the data randomly into 8:1:1 as the training set, validation set, and test set, respectively. 

  The dataset statistics are summarized as follows:

  | Dataset  | Total | #Train | #Validation | #Test | 
  | :--------: | :-----: |:-----: | :----------: | :----: | 
  | Avazu_x4 |  40,428,967     |  32,343,172   |  4,042,897     | 4,042,898     |  


  - Avazu_x4_001

    In this setting, we preprocess the data split by removing the ``id`` field that is useless for CTR prediction. In addition, we transform the timestamp field into three fields: hour, weekday, and is_weekend. For all categorical fields, we filter infrequent features by setting the threshold min_category_count=2 (performs well) and replace them with a default ``<OOV>`` token. Note that we do not follow the exact preprocessing steps in AutoInt, because the authors neither remove the useless ``id`` field nor specially preprocess the timestamp field. We fix **embedding_dim=16** following the existing [AutoInt work](https://arxiv.org/abs/1810.11921).
    
  - Avazu_x4_002

    In this setting, we preprocess the data split by removing the ``id`` field that is useless for CTR prediction. In addition, we transform the timestamp field into three fields: hour, weekday, and is_weekend. For all categorical fields, we filter infrequent features by setting the threshold min_category_count=1 and replace them with a default ``<OOV>`` token. Note that we found that min_category_count=1 performs the best, which is surprising. We fix **embedding_dim=40** following the existing [FGCNN work](https://arxiv.org/abs/1904.04447).


+ **Source:** https://www.kaggle.com/c/avazu-ctr-prediction/data
+ **Download:** https://huggingface.co/datasets/reczoo/Avazu_x4/tree/main
+ **RecZoo Datasets:** https://github.com/reczoo/Datasets

+ **Used by papers:** 
  - Weiping Song, Chence Shi, Zhiping Xiao, Zhijian Duan, Yewen Xu, Ming Zhang, Jian Tang. [AutoInt: Automatic Feature Interaction Learning via Self-Attentive Neural Networks](https://arxiv.org/abs/1810.11921). In CIKM 2019.
  - Jieming Zhu, Jinyang Liu, Shuai Yang, Qi Zhang, Xiuqiang He. [BARS-CTR: Open Benchmarking for Click-Through Rate Prediction](https://arxiv.org/abs/2009.05794). In CIKM 2021.
  
+ **Check the md5sum for data integrity:**
  ```bash
  $ md5sum train.csv valid.csv test.csv
  de3a27264cdabf66adf09df82328ccaa  train.csv
  33232931d84d6452d3f956e936cab2c9  valid.csv
  3ebb774a9ca74d05919b84a3d402986d  test.csv
  ```
