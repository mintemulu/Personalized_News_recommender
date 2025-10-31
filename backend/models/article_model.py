def serialize_article(article):
    return {
        "id": str(article.get("_id")),
        "title": article.get("title"),
        "description": article.get("description"),
        "url": article.get("url"),
        "source": article.get("source"),
        "category": article.get("category"),
        "keywords": article.get("keywords", [])
    }
