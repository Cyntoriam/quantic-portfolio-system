# Quantic Portfolio System

A portfolio starter with a FastAPI backend, a PostgreSQL schema, and a responsive
single-page frontend with a metallic gold and fuchsia visual direction.

## Project structure

```text
quantic-portfolio-system/
├── backend/
│   └── main.py
├── database/
│   └── schema.sql
├── frontend/
│   └── index.html
└── README.md
```

## Components

- **Backend:** `backend/main.py` defines the FastAPI app, Pydantic-validated
  portfolio models, a health check, and a starter portfolio endpoint.
- **Database:** `database/schema.sql` creates relational tables for portfolio
  projects and contact messages, with constraints and useful indexes.
- **Frontend:** `frontend/index.html` is a responsive, dependency-free portfolio
  page. Project cards and contact details are sample content; replace them with
  your own work and email address before publishing.

## Run the API

Install FastAPI and an ASGI server in your Python environment, then run:

```bash
uvicorn main:app --reload --app-dir backend
```

The API is available at `http://127.0.0.1:8000`. Interactive API documentation
is at `/docs`; `/api/health` checks service availability and `/api/portfolio`
returns the validated starter portfolio.

## Set up the database

Create a PostgreSQL database, then apply the schema:

```bash
psql "$DATABASE_URL" -f database/schema.sql
```

The current API serves starter portfolio data in memory. Database connectivity
and persistence are not configured yet.

## Quantic submission notes

The frontend is a static portfolio prototype. Personalize the profile,
projects, and contact link, and connect the API and database when preparing a
production submission.
