# Carbon Trace Kenya

AI-powered transport emission disclosure platform for Kenyan institutions. Built for the EPRA Hackathon 2026 by Team EmitIQ.

## Stack

- **Backend**: FastAPI (Python) with SQLAlchemy, PostgreSQL, Redis, RQ
- **Frontend**: React 19 + Vite + Tailwind CSS + Recharts
- **ML**: Isolation Forest (anomaly detection), GHG Protocol calculation engine

## Quick Start (Local)

```bash
# Backend
pip install -r requirements.txt
uvicorn carbontrace-backend.main:app --reload

# Frontend
cd carbontrace
npm install
npm run dev

# Worker (background jobs)
python worker.py
```

## Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)

1. Fork or push this repo to GitHub
2. Create a new project on [Railway](https://railway.app)
3. Connect your GitHub repo
4. Add these plugins:
   - **PostgreSQL** (free tier)
   - **Redis** (free tier)
5. Set environment variables:
   - `JWT_SECRET` — generate with `python -c "import secrets; print(secrets.token_urlsafe(32))"`
   - `GEMINI_API_KEY` — get from https://aistudio.google.com/apikey (for OCR/chatbot)
6. Railway auto-detects `Dockerfile` and `railway.json` — deploy starts automatically

### Railway Services

| Service | Source | Port |
|---------|--------|------|
| Backend | `Dockerfile` (root) | 8000 |
| Frontend | `carbontrace/Dockerfile` | 5173 |
| PostgreSQL | Railway plugin | 5432 |
| Redis | Railway plugin | 6379 |

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | Yes | Auto-set by Railway PostgreSQL plugin |
| `REDIS_URL` | Yes | Auto-set by Railway Redis plugin |
| `JWT_SECRET` | Yes | Secret key for JWT tokens |
| `GEMINI_API_KEY` | No | Google Gemini API key (OCR + chatbot) |
| `USE_S3` | No | Set to `true` for S3 storage |

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /health` | Health check |
| `GET /metrics` | Prometheus metrics |
| `GET /api/overview/kpis` | Dashboard KPIs |
| `GET /api/overview/quarterly-trend` | Quarterly emission trends |
| `GET /api/calculator/results` | GHG calculation results |
| `GET /api/reconcile/flags` | Anomaly flags |
| `POST /api/ingestion/upload` | Upload CSV data |
| `POST /api/ingestion/upload-image` | Upload image for OCR |
| `POST /api/chat` | Gemini-powered chatbot |
| `GET /api/epra/kpis` | EPRA sector analytics |

## Contributors

- Muchiri Timothy Gitau — Team Lead & Backend AI Engineer
- Collins Njuguna Ndung'u
- Erick Neko
- Maxwell Muthee
- Team EmitIQ — EPRA Hackathon 2026
