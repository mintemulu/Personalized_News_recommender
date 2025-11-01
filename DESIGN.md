# Short Design Explanation

## Data flow & architecture

The frontend (React) collects a comma‑separated list of interests and sends them to the FastAPI backend (`POST /api/recommend`). A separate ingestion endpoint (`GET /api/fetch`) retrieves ~50 recent articles from NewsAPI, normalizes fields, and stores/updates them in MongoDB (collection `articles`, key is `url`). During ingestion, spaCy (`en_core_web_sm`) extracts keywords from each article’s title+description. The backend recommendation logic computes a simple overlap score between the user’s interests and an article’s stored keywords, returning the top 5 matches via JSON. CORS is enabled to allow the Vite dev server to call the API.

## Trade-offs & simplifications

- Simplicity over semantics: a bag‑of‑words approach (single‑token NOUN/PROPN lemmas) is fast and dependency‑light but misses multi‑word phrases (e.g., “renewable energy”) and abbreviations (e.g., “AI”).
- Exact matching: overlap scoring is interpretable and efficient but can yield lower recall than embeddings or fuzzy matching.
- Schemaless storage: MongoDB enables quick iteration (upsert by `url`) without migrations, at the cost of weaker relational guarantees.
- Source & coverage: NewsAPI provides broad, recent coverage; quality depends on its upstream sources and rate limits.
- Extensibility: can evolve to phrase extraction, TF‑IDF/embedding similarity, per‑user profiles, scheduling/cron ingestion, and filtering by category/source.
