from typing import Dict, List
from collections import Counter
import httpx

from .schemas import FilmShortModel, FilmStatus
from .config import Config


class RecommendService:

    async def getRecommendations(
        self, films: List[FilmShortModel]
    ) -> List[FilmShortModel]:

        seenIds = {film.id for film in films}

        count: Dict = Counter(genre.name for film in films for genre in film.genres)
        topGenres = [gnr[0] for gnr in count.most_common(2)]

        if not topGenres:
            return []

        query_params = "&".join([f"genres.name={genre}" for genre in topGenres])

        url = f"https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&{query_params}"

        headers = {"X-API-KEY": Config.KINOPOISK_API_KEY}

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)

        filmsData: List[dict] = response.json()["docs"]

        filteredFilms = [film for film in filmsData if film["id"] not in seenIds]

        filteredFilms.sort(key=lambda x: x["rating"]["kp"], reverse=True)

        recommendations = [
            FilmShortModel(
                id=film["id"],
                title=film.get("name") or film.get("alternativeName") or film.get("enName") or "Неизвестно",
                year=film["year"],
                genres=film["genres"],
                poster=film.get("poster", {}).get("url", ""),
                status=FilmStatus.PLANNED
            )
            for film in filteredFilms
        ]

        return recommendations

