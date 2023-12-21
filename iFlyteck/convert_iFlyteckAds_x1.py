import pandas as pd
from collections import Counter
import random

train_file = "train_data.txt"
test_file = "test_data.txt"

columns = ['label'] + ["f{}".format(i + 1) for i in range(245)]
train_data = pd.read_csv(train_file, header=None, names=columns, dtype=object, memory_map=True)
train_data.drop([1613993, 1895025], 0, inplace=True) # drop abnormal rows
num_train = len(train_data)
test_data = pd.read_csv(test_file, header=None, names=columns[1:], dtype=object, memory_map=True)
test_data[columns[0]] = [0] * len(test_data)
num_test = len(test_data)
all_data = pd.concat([train_data, test_data], sort=False).reset_index(drop=True)
all_data["label"] = all_data["label"].astype(int)
print("num_train, num_test:", num_train, num_test)

for col in ["f1", "f2", "f3", "f4"]:
    col_dict = Counter(all_data[col])
    vocab = dict(zip(col_dict.keys(), range(len(col_dict))))
    all_data[col] = all_data[col].map(lambda x: vocab[x])
print(all_data.head())

train_df = all_data.iloc[0:num_train, :].reset_index(drop=True)
test_df = all_data.iloc[num_train:, :]

def get_statistics_by_slotid(df, fout):
    slotid_impressions = df.groupby(['f1'])['f1'].count()
    slotid_clicks = df.groupby(['f1'])['label'].sum()
    slotid_impressions.to_csv(fout + "_slotid_impressions.csv")
    slotid_clicks.to_csv(fout + "_slotid_clicks.csv")

get_statistics_by_slotid(train_df, "train_all")
get_statistics_by_slotid(test_df, "test")

# train-validation-test splitting
sample_index = list(range(num_train))
random.seed(2022)
random.shuffle(sample_index)
train_index = sample_index[0:int(num_train * 0.9)]
valid_index = sample_index[int(num_train * 0.9):]
valid_df = train_df.iloc[valid_index, :]
train_df = train_df.iloc[train_index, :]
train_df.to_csv("train.csv", index=False)
valid_df.to_csv("valid.csv", index=False)
test_df.to_csv("test.csv", index=False)
print("train:valid:test samples:", len(train_df), len(valid_df), len(test_df))

get_statistics_by_slotid(train_df, "train")
get_statistics_by_slotid(valid_df, "valid")
print("All done.")
