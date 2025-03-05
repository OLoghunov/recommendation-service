from typing import Dict, List
from collections import Counter
import logging

from .schemas import FilmShortModel



class RecommendService:

    async def getRecommendations(self, films: List[FilmShortModel]) -> List[FilmShortModel]:
        
        count: Dict = Counter(genre.name for film in films for genre in film.genres)   
        return []
        