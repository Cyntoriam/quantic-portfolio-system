"""FastAPI entry point for the Quantic portfolio system."""

from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict, Field, HttpUrl
from sqlalchemy import Integer, String, Text, text
from sqlalchemy.orm import Mapped, Session, mapped_column

from backend.database import Base, get_db

app = FastAPI(
    title="Dr. Cyntoria Meaderds Portfolio API",
    description="Portfolio and technical certification data backed by PostgreSQL.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Project(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: Annotated[str, Field(min_length=1, max_length=100)]
    description: Annotated[str, Field(min_length=1, max_length=500)]
    category: Annotated[str, Field(min_length=1, max_length=60)]
    technologies: Annotated[list[str], Field(min_length=1, max_length=12)]
    href: HttpUrl | None = None


class Portfolio(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: Annotated[str, Field(min_length=1, max_length=100)]
    role: Annotated[str, Field(min_length=1, max_length=120)]
    introduction: Annotated[str, Field(min_length=1, max_length=500)]
    projects: Annotated[list[Project], Field(max_length=50)]


class CertificationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    issuer: str
    score_details: str | None = None
    description: str
    badge_image_url: HttpUrl | None = None
    credential_url: HttpUrl | None = None


class CertificationModel(Base):
    __tablename__ = "certifications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    issuer: Mapped[str] = mapped_column(String(100), nullable=False)
    score_details: Mapped[str | None] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text, nullable=False)
    badge_image_url: Mapped[str | None] = mapped_column(String(255))
    credential_url: Mapped[str | None] = mapped_column(String(255), unique=True)


portfolio = Portfolio(
    name="Your Name",
    role="Independent designer & developer",
    introduction=(
        "I shape thoughtful digital experiences, bringing considered design "
        "and purposeful technology together."
    ),
    projects=[],
)


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/health")
def versioned_health_check(db: Session = Depends(get_db)) -> dict[str, str]:
    db.execute(text("SELECT 1"))
    return {
        "status": "healthy",
        "system": "PostgreSQL & FastAPI Backend Active",
    }


@app.get("/api/portfolio", response_model=Portfolio)
def get_portfolio() -> Portfolio:
    return portfolio


@app.get(
    "/api/v1/certifications",
    response_model=list[CertificationResponse],
    summary="Retrieve Certifications from PostgreSQL",
)
def get_certifications(db: Session = Depends(get_db)) -> list[CertificationModel]:
    return db.query(CertificationModel).order_by(CertificationModel.id).all()
