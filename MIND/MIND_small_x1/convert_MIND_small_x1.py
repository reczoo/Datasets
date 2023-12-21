import pandas as pd
import numpy as np
import h5py
import os
import hashlib

MAX_SEQ_LEN = 50
train_path = "./MINDsmall_train/"
dev_path = "./MINDsmall_dev/"

print("Preprocess news profile...")
train_wiki_file = os.path.join(train_path, "entity_embedding.vec")
dev_wiki_file = os.path.join(dev_path, "entity_embedding.vec")
entity_dict = dict()
with open(train_wiki_file, "r") as fin:
    for line in fin:
        l = line.strip().split("\t")
        entity_dict[l[0]] = [float(v) for v in l[1:]]
with open(dev_wiki_file, "r") as fin:
    for line in fin:
        l = line.strip().split("\t")
        entity_dict[l[0]] = [float(v) for v in l[1:]]

train_news_file = os.path.join(train_path, "news.tsv")
train_news = pd.read_csv(train_news_file, sep="\t", header=None,
                         names=["news_id", "cat", "sub_cat", "title", "abstract", "url", 
                         "title_entities", "abstract_entities"])
dev_news_file = os.path.join(dev_path, "news.tsv")
dev_news = pd.read_csv(dev_news_file, sep="\t", header=None,
                       names=["news_id", "cat", "sub_cat", "title", "abstract", "url", 
                       "title_entities", "abstract_entities"])
news = pd.concat([train_news, dev_news], axis=0)
news = news.drop_duplicates(subset=['news_id']).reset_index(drop=True)
news = news[["news_id", "cat", "sub_cat", "title_entities", "abstract_entities", "title", "abstract"]]
news["title_entities"] = news["title_entities"].fillna("[]")
news["abstract_entities"] = news["abstract_entities"].fillna("[]")
news["title_entities"] = news["title_entities"] \
    .map(lambda x: "^".join([v["WikidataId"] for v in eval(x) if v["WikidataId"] in entity_dict]))
news["abstract_entities"] = news["abstract_entities"] \
    .map(lambda x: "^".join([v["WikidataId"] for v in eval(x) if v["WikidataId"] in entity_dict]))
news.to_csv("news_corpus.tsv", sep="\t", index=False)
print(news.head())

entity_set = set(list(news["title_entities"].values) + list(news["abstract_entities"].values))
entity_keys = []
entity_values = []
for k, v in entity_dict.items():
    if k in entity_set:
        entity_keys.append(k)
        entity_values.append(v)
with h5py.File("entity_emb_dim100.h5", 'w') as hf:
    hf.create_dataset("key", data=np.array(entity_keys, dtype=h5py.special_dtype(vlen=str)))
    hf.create_dataset("value", data=np.array(entity_values))

news2cat = dict(zip(news["news_id"], news["cat"]))
news2subcat = dict(zip(news["news_id"], news["sub_cat"]))
news2title_entities = dict(zip(news["news_id"], news["title_entities"]))
news2abstract_entities = dict(zip(news["news_id"], news["abstract_entities"]))
used_feat = [
    "imp_id",
    "click",
    "hour",
    "user_id", 
    "news_id",
    "cat",
    "sub_cat",
    "title_entities",
    "abstract_entities",
    "news_his",
    "cat_his",
    "subcat_his"
]

def join_data(in_path, out_path):
    df = pd.read_csv(in_path, sep="\t", header=None, 
                     names=["imp_id", "user_id", "timestamp", "news_his", "impression_list"])
    df["news_his"] = df["news_his"].fillna("").map(lambda x: \
        "^".join([v for v in x.split() if v in news2cat][-MAX_SEQ_LEN:]))
    df = df.drop('impression_list', axis=1).join( \
            df['impression_list'].str.split(' ', expand=True).stack(). \
            reset_index(level=1, drop=True).rename('impression'))
    df["hour"] = df["timestamp"].map(lambda t: t.split(" ")[1].split(":")[0] + t.split(" ")[-1])
    df[["news_id", "click"]] = df["impression"].str.split("-", expand=True)
    df = pd.merge(df, news, how="left", on="news_id")
    df["cat_his"] = df["news_his"].map(lambda x: "^".join([news2cat.get(i, "") for i in x.split("^")]))
    df["subcat_his"] = df["news_his"].map(lambda x: "^".join([news2subcat.get(i, "") for i in x.split("^")]))
    df[used_feat].to_csv(out_path, index=False)

print("Preprocess train data...")
join_data(os.path.join(train_path, "behaviors.tsv"), "train.csv")
print("Preprocess dev data...")
join_data(os.path.join(dev_path, "behaviors.tsv"), "valid.csv")

# Check md5sum for correctness
assert("fe0ec15c20424535b5e5471a7f32d61e" == hashlib.md5(open('news_corpus.tsv', 'r').read().encode('utf-8')).hexdigest())
assert("18b16481ad421986de3f80ce3295f5ed" == hashlib.md5(open('train.csv', 'r').read().encode('utf-8')).hexdigest())
assert("1223a2a14fa65e880bc8158836da3894" == hashlib.md5(open('valid.csv', 'r').read().encode('utf-8')).hexdigest())
print("Reproducing data succeeded!")
