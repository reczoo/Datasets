# KKBox_x1

+ **Dataset description:**
  
  KKBox is a challenge dataset for music recommendation at WSDM 2018. The data consist of user-song pairs in a given time period, with a total of 19 user features (e.g., city, gender) and song features (e.g., language, genre, artist). We randomly split the data into 8:1:1 as the training set, validation set, and test set, respectively. In this setting, for all categorical fields, we replace infrequent features with a default ``<OOV>`` token by setting the threshold min_category_count=10.

  The dataset statistics are summarized as follows:

  | Dataset Split  | Total | #Train | #Validation | #Test | 
  | :--------: | :-----: |:-----: | :----------: | :----: | 
  | KKBox_x1 |  7,377,418   | 5,901,932  |  737,743    | 737,743    |

+ **Source:** https://www.kaggle.com/c/kkbox-music-recommendation-challenge
+ **Download:** https://huggingface.co/datasets/reczoo/KKBox_x1/tree/main
+ **RecZoo Datasets:** https://github.com/reczoo/Datasets

+ **Used by papers:** 
  - Jieming Zhu, Quanyu Dai, Liangcai Su, Rong Ma, Jinyang Liu, Guohao Cai, Xi Xiao, Rui Zhang. [BARS: Towards Open Benchmarking for Recommender Systems](https://arxiv.org/abs/2205.09626). In SIGIR 2022.

+ **Check the md5sum for data integrity:**
  ```bash
  $ md5sum train.csv valid.csv test.csv
  195b1ae8fc2d9267d7c8656c07ea1304  train.csv
  398e97ac139611a09bd61a58e4240a3e  valid.csv
  8c5f7add05a6f5258b6b3bcc00ba640b  test.csv
  ```
