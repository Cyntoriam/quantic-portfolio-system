# Quantic Portfolio System

A portfolio starter with a FastAPI backend, a PostgreSQL schema, and a responsive
single-page frontend with a metallic gold and fuchsia visual direction.

## Project structure

```text
quantic-portfolio-system/
├── backend/
│   ├── database.py
│   └── main.py
├── database/
│   └── schema.sql
├── frontend/
│   └── index.html
├── requirements.txt
└── README.md
```

## Components

- **Backend:** `backend/main.py` defines the FastAPI app, Pydantic-validated
  portfolio and certification models, health checks, and portfolio and
  certification endpoints. The public API permits cross-origin requests;
  credentialed CORS requests are disabled. `backend/database.py` configures the
  SQLAlchemy engine and request-scoped database session dependency.
- **Database:** `database/schema.sql` creates relational tables for portfolio
  projects and contact messages, with constraints and useful indexes.
- **Frontend:** `frontend/index.html` is a responsive, dependency-free portfolio
  page that loads certification cards from the local API. Project cards and
  contact details are sample content; replace them with your own work and email
  address before publishing.

## Run the API

Install the pinned dependencies and start the API:

```bash
pip install -r requirements.txt
uvicorn main:app --reload --app-dir backend --port 8001
```

The API is available at `http://127.0.0.1:8001`. Interactive API documentation
is at `http://127.0.0.1:8001/docs`; `/api/health` checks service availability
and `/api/portfolio` returns the validated starter portfolio.
`/api/v1/certifications` returns technical certification data, while
`/api/v1/health` provides the versioned health check.

## Set up the database

Create a PostgreSQL database, then apply the schema:

```bash
psql "$DATABASE_URL" -f database/schema.sql
```

The certifications endpoint reads from PostgreSQL. Applying the schema creates
the certifications table and inserts the sample AMD certification if it is not
already present. The portfolio endpoint still serves starter data in memory.
Set `DATABASE_URL` to override the local PostgreSQL connection string used by
`backend/database.py`.

## Quantic submission notes

The frontend is a static portfolio prototype. Personalize the profile,
projects, and contact link, and connect the API and database when preparing a
production submission.
