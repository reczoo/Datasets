# KuaiVideo_x1

+ **Dataset description:**
  
  The raw dataset is released by the Kuaishou Competition in the China MM 2018 conference, which aims to predict users' click probabilities for new micro-videos. In this dataset, there are multiple types of interactions between users and micro-videos, such as "click", "not click", "like", and "follow". Particularly, "not click" means the user did not click the micro-video after previewing its thumbnail. Note that the timestamp associated with each behaviour has been processed such that the absolute time is unknown, but the sequential order can be obtained according to the timestamp. For each micro-video, we can access its 2,048-d visual embedding of its thumbnail. In total, 10,000 users and their 3,239,534 interacted micro-videos are randomly selected. We follow the train-test data splitting from the [ALPINE](https://github.com/liyongqi67/ALPINE) work. In this setting, we filter infrequent categorical features with the threshold min_category_count=10. We further set the maximal length of user behavior sequence to 100.

  The dataset statistics are summarized as follows:

  | Dataset Split  | Total | #Train | #Validation | #Test | 
  | :--------: | :-----: |:-----: | :----------: | :----: | 
  | KuaiVideo_x1 | 13,661,383    | 10,931,092  |      | 2,730,291   |

+ **Source:** https://www.kuaishou.com/activity/uimc
+ **Download:** https://huggingface.co/datasets/reczoo/KuaiVideo_x1/tree/main
+ **RecZoo Datasets:** https://github.com/reczoo/Datasets

+ **Used by papers:**
  - Yongqi Li, Meng Liu, Jianhua Yin, Chaoran Cui, Xinshun-Xu, and Liqiang Nie. [Routing Micro-videos via A Temporal Graph-guided Recommendation System](https://liyongqi67.github.io/papers/MM2019_Routing_Micro_videos_via_A_Temporal_Graph_guided_Recommendation_System.pdf). In MM 2020.
  - Jieming Zhu, Guohao Cai, Junjie Huang, Zhenhua Dong, Ruiming Tang, Weinan Zhang. [ReLoop2: Building Self-Adaptive Recommendation Models via Responsive Error Compensation Loop](https://arxiv.org/abs/2306.08808). In KDD 2023.

+ **Check the md5sum for data integrity:**
  ```bash
  $ md5sum train.csv test.csv
  16f13734411532cc313caf2180bfcd56  train.csv
  ba26c01caaf6c65c272af11aa451fc7a  test.csv
  ```
