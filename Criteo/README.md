# Criteo

+ [Criteo_x1](./Criteo_x1)
+ [Criteo_x2](./Criteo_x2)
+ [Criteo_x4](./Criteo_x4)

The dataset is from a [Kaggle challenge for Criteo display advertising](https://www.kaggle.com/c/criteo-display-ad-challenge/data). Criteo is a personalized retargeting company that works with Internet retailers to serve personalized online display advertisements to consumers. The goal of this Kaggle challenge is to predict click-through rates on display ads. It offers a week's worth of data from Criteo's traffic. In the labeled training set over a period of 7 days, each row corresponds to a display ad served by Criteo. The samples are chronologically ordered. Positive and negatives samples have both been subsampled at different rates in order to reduce the dataset size. There are 13 count features and 26 categorical features. The semantic of these features is undisclosed. Some feature have missing values. Note that only the labeled part (i.e., `train.txt`) of the data is used for benchmarking. 

Data fields consist of:
+ Label: Target variable that indicates if an ad was clicked (1) or not (0).
+ I1-I13: A total of 13 columns of integer features (mostly count features).
+ C1-C26: A total of 26 columns of categorical features. The values of these features have been hashed onto 32 bits for anonymization purposes. 
