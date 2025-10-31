from dotenv import load_dotenv
load_dotenv()

from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["news_recommender"]
articles_collection = db["articles"]
