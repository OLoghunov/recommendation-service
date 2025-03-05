from typing import List

from fastapi import APIRouter

from .schemas import FilmShortModel
from .service import RecommendService

recommendRouter = APIRouter()
recommendService = RecommendService()


@recommendRouter.post("/films", response_model=List[FilmShortModel])
async def get_recommendations(films: List[FilmShortModel]):
    
    return await recommendService.getRecommendations(films)