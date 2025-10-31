# Personalized News Recommender - Setup

## Backend (FastAPI)
1) Configure env in `backend/.env`:
   - `MONGO_URI=mongodb://localhost:27017/`
   - `NEWSAPI_KEY=<your NewsAPI key>`

2) Install Python deps:
   - Windows PowerShell:
     - `backend\venv\Scripts\python.exe -m pip install -r backend\requirements.txt`

3) Install spaCy model (auto on first run; manual if needed):
   - `backend\venv\Scripts\python.exe -m spacy download en_core_web_sm`

4) Run the API (port 8000):
   - `backend\venv\Scripts\python.exe -m uvicorn main:app --app-dir backend --host 0.0.0.0 --port 8000 --reload`
   - Health: GET http://localhost:8000/ → `{ "message": "News Recommender API running" }`

5) Ingest data (~50 articles):
   - GET http://localhost:8000/api/fetch

6) Get recommendations (top 5):
   - POST http://localhost:8000/api/recommend
   - Body: JSON array of lowercase single-word interests, e.g. `["energy", "bitcoin"]`

## Frontend (React + Vite)
1) Install deps:
   - `cd frontend`
   - `npm install`

2) Run dev server (defaults to http://localhost:5173):
   - `npm run dev`

The UI accepts interests, calls the backend, and renders recommended articles.

---

## NLP approach and design choices
- NLP: spaCy `en_core_web_sm` to extract keywords from title+description. We keep lemmatized, lowercase, alphabetic tokens that are NOUN/PROPN and length > 2; duplicates removed.
- Scoring: simple keyword overlap between user interests and article keywords; return top 5.
- Design choices: MongoDB for schemaless storage and easy upserts by `url`; FastAPI for a small, typed API; NewsAPI as source; permissive CORS for local dev; minimal React UI focused on the flow.
- Known limitations: matches only single words (multi-word phrases like "renewable energy" won’t match as a phrase); abbreviations (e.g., "AI") and stopwords are often excluded by POS/filters; exact-token matching (no fuzzy semantics).

See `DESIGN.md` for a short data-flow/architecture summary and trade-offs.
