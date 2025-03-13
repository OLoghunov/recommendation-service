from typing import List

from fastapi import APIRouter

from .schemas import FilmShortModel
from .service import RecommendService

recommend_router = APIRouter()
recommend_service = RecommendService()


@recommend_router.post("/films", response_model=List[FilmShortModel])
async def get_recommendations(films: List[FilmShortModel]):

    return await recommend_service.get_recommendations(films)
