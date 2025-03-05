from typing import List, Optional
from enum import Enum

from pydantic import BaseModel, Field


class FilmStatus(str, Enum):
    WATCHED = "watched"
    PLANNED = "planned"


class GenreModel(BaseModel):
    name: str = Field(...)


class FilmShortModel(BaseModel):
    id: int
    title: str = Field(...)
    year: Optional[int] = Field(default=None)
    genres: List[GenreModel] = Field(alias="genres")
    poster: Optional[str] = Field(None)
    status: FilmStatus
    tmdbId: Optional[int] = Field(default=None)
