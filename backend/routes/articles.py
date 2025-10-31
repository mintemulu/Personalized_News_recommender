from dotenv import load_dotenv
load_dotenv()
from fastapi import APIRouter, HTTPException
import os
import requests
from db import articles_collection
from nlp_utils import extract_keywords

router = APIRouter()

@router.get("/fetch")
def fetch_articles():
    newsapi_key = os.getenv("NEWSAPI_KEY")
    if not newsapi_key:
        raise HTTPException(status_code=400, detail="NEWSAPI_KEY not set in environment/.env")

    url = "https://newsapi.org/v2/everything"
    params = {
        "language": "en",
        "pageSize": 50,
        "sortBy": "publishedAt",
        # basic broad query to get recent items
        "q": "news",
        "apiKey": newsapi_key,
    }

    try:
        res = requests.get(url, params=params, timeout=20)
        res.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch articles: {e}")

    data = res.json() or {}
    articles = data.get("articles", [])

    saved = 0
    for a in articles:
        title = a.get("title") or ""
        description = a.get("description") or ""
        url = a.get("url")
        if not url:
            continue
        doc = {
            "title": title,
            "description": description,
            "url": url,
            "source": (a.get("source") or {}).get("name"),
            "category": "general",
            "keywords": extract_keywords(f"{title} {description}")
        }
        articles_collection.update_one({"url": url}, {"$set": doc}, upsert=True)
        saved += 1

    return {"message": f"{saved} articles fetched and stored."}
