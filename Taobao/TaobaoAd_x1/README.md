# TaobaoAd_x1

+ **Dataset description:**
  
  Taobao is a dataset provided by Alibaba, which contains 8 days of ad click-through data (26 million records) that are randomly sampled from 1140000 users. By default, the first 7 days (i.e., 20170506-20170512) of samples are used as training samples, and the last day's samples (i.e., 20170513) are used as test samples. Meanwhile, the dataset also covers the shopping behavior of all users in the recent 22 days, including totally seven hundred million records. We follow the preprocessing steps that have been applied to [reproducing the DMR work](https://aistudio.baidu.com/aistudio/projectdetail/1805731). We note that a small part (~5%) of samples have been dropped during preprocessing due the missing of user or item profiles. In this setting, we filter infrequent categorical features with the threshold min_category_count=10. We further set the maximal length of user behavior sequence to 50.

  The dataset statistics are summarized as follows:

  | Dataset Split  | Total | #Train | #Validation | #Test | 
  | :--------: | :-----: |:-----: | :----------: | :----: | 
  | TaobaoAd_x1 | 25,029,426     | 21,929,911  |      | 3,099,515    |

+ **Data format:**
    + user: User ID (int);
    + time_stamp: time stamp (Bigint, 1494032110 stands for 2017-05-06 08:55:10);
    + adgroup_id: adgroup ID (int);
    + pid: scenario;
    + noclk: 1 for not click, 0 for click;
    + clk: 1 for click, 0 for not click;

    ad_feature:
    + adgroup_id: Ad ID (int);
    + cate_id: category ID;
    + campaign_id: campaign ID;
    + brand: brand ID;
    + customer_id: Advertiser ID;
    + price: the price of item

    user_profile:
    + userid: user ID;
    + cms_segid: Micro group ID;
    + cms_group_id: cms group_id;
    + final_gender_code: gender 1 for male, 2 for female
    + age_level: age_level
    + pvalue_level: Consumption grade, 1: low, 2: mid, 3: high
    + shopping_level: Shopping depth, 1: shallow user, 2: moderate user, 3: depth user
    + occupation: Is the college student 1: yes, 0: no?
    + new_user_class_level: City level

    raw_behavior_log:
    + nick: User ID(int);
    + time_stamp: time stamp (Bigint, 1494032110 stands for 2017-05-06 08:55:10);
    + btag: Types of behavior, include: ipv/cart/fav/buy;
    + cate: category ID(int);
    + brand: brand ID(int);

+ **Source:** https://tianchi.aliyun.com/dataset/dataDetail?dataId=56
+ **Download:** https://huggingface.co/datasets/reczoo/TaobaoAd_x1/tree/main
+ **RecZoo Datasets:** https://github.com/reczoo/Datasets

+ **Used by papers:**
  - Ze Lyu, Yu Dong, Chengfu Huo, Weijun Ren. [Deep Match to Rank Model for Personalized Click-Through Rate Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/5346). In AAAI 2020.

+ **Check the md5sum for data integrity:**
  ```bash
  $ md5sum train.csv test.csv
  eaabfc8629f23519b04593e26c7522fc  train.csv
  f5ae6197e52385496d46e2867c1c8da1  test.csv
  ```
