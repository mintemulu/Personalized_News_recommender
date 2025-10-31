from dotenv import load_dotenv
load_dotenv()
import os, json
from pymongo import MongoClient
from collections import Counter

uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(uri)
col = client["news_recommender"]["articles"]

keywords = []
for a in col.find({}, {"keywords": 1}):
    kws = a.get("keywords") or []
    keywords.extend(kws)

unique = sorted(set(keywords))
freq = Counter(keywords).most_common(50)

print(json.dumps({
    "unique_count": len(unique),
    "sample_unique": unique[:100],
    "top_keywords": freq
}, ensure_ascii=False, indent=2))
