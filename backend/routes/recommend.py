from fastapi import APIRouter, Body
from db import articles_collection
from models.article_model import serialize_article


router = APIRouter()

@router.post("/recommend")
def recommend_articles(interests: list[str] = Body(...)):
    pipeline = []
    results = []
    for article in articles_collection.find():
        keywords = article.get("keywords", [])
        score = len(set(interests).intersection(set(keywords)))
        if score > 0:
            article["score"] = score
            results.append(article)
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)[:5]
    return [serialize_article(a) for a in sorted_results]
