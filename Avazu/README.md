# Avazu

+ [Avazu_x1](./Avazu_x1/README.md)
+ [Avazu_x2](./Avazu_x2/README.md)
+ [Avazu_x4](./Avazu_x4/README.md)

It is a [Kaggle challenge dataset](https://www.kaggle.com/c/avazu-ctr-prediction/data) for Avazu CTR prediction. [Avazu](http://avazuinc.com/home) is one of the leading mobile advertising platforms globally. The Kaggle competition targets at predicting whether a mobile ad will be clicked and has provided 11 days worth of Avazu data to build and test prediction models. It consists of 10 days of labeled click-through data for training and 1 day of ads data for testing (yet without labels). Note that only the first 10 days of labeled data are used for benchmarking. 

Data fields consist of:
+ id: ad identifier (``Note: This column is more like unique sample id, where each row has a distinct value, and thus should be dropped.``)
+ click: 0/1 for non-click/click
+ hour: format is YYMMDDHH, so 14091123 means 23:00 on Sept. 11, 2014 UTC. (``Note: It is a common practice to bucketize the timestamp into hour, day, is_weekend, and so on.``)
+ C1: anonymized categorical variable
+ banner_pos
+ site_id
+ site_domain
+ site_category
+ app_id
+ app_domain
+ app_category
+ device_id
+ device_ip
+ device_model
+ device_type
+ device_conn_type
+ C14-C21: anonymized categorical variables
