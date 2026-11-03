"""FastAPI entry point for the Quantic portfolio system."""

from typing import Annotated

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field, HttpUrl

app = FastAPI(
    title="Quantic Portfolio API",
    description="Validated portfolio content for the Quantic portfolio system.",
    version="1.0.0",
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


@app.get("/api/portfolio", response_model=Portfolio)
def get_portfolio() -> Portfolio:
    return portfolio