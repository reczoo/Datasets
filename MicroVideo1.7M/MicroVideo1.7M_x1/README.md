# MicroVideo1.7M_x1

+ **Dataset description:**
  
  This is a micro-video dataset provided by the [THACIL work](https://dl.acm.org/doi/10.1145/3240508.3240617), which contains 12,737,617 interactions that 10,986 users have made on 1,704,880 micro-videos. The features include user id, item id, category, and the extracted image embedding vectors of cover images of micro-videos. Note that the dataset has been split such that the items in the test set are all new micro-videos, which have no overlap with the items in the training set. This helps validate the generability of multimodal embedding vectors for new micro-videos. In this setting, we set the maximal length of user behavior sequence to 100.

  The dataset statistics are summarized as follows:

  | Dataset Split  | Total | #Train | #Validation | #Test | 
  | :--------: | :-----: |:-----: | :----------: | :----: | 
  | MicroVideo1.7M_x1 |  12,737,617    | 8,970,309  |      | 3,767,308    | 

+ **Source:** https://github.com/Ocxs/THACIL
+ **Download:** https://huggingface.co/datasets/reczoo/MicroVideo1.7M_x1/tree/main
+ **RecZoo Datasets:** https://github.com/reczoo/Datasets

+ **Used by papers:**
  - Xusong Chen, Dong Liu, Zheng-Jun Zha, Wengang Zhou, Zhiwei Xiong, Yan Li. [Temporal Hierarchical Attention at Category- and Item-Level for Micro-Video Click-Through Prediction](https://dl.acm.org/doi/10.1145/3240508.3240617). In MM 2018.
  - Jieming Zhu, Guohao Cai, Junjie Huang, Zhenhua Dong, Ruiming Tang, Weinan Zhang. [ReLoop2: Building Self-Adaptive Recommendation Models via Responsive Error Compensation Loop](https://arxiv.org/abs/2306.08808). In KDD 2023.

+ **Check the md5sum for data integrity:**
  ```bash
  $ md5sum train.csv test.csv
  936e6612714c887e76226a60829b4e0a  train.csv
  9417a18304fb62411ac27c26c5e0de56  test.csv
  ```
