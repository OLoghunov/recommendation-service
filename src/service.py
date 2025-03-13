from typing import Dict, List
from collections import Counter
import httpx

from .schemas import FilmShortModel, FilmStatus
from .config import Config


class RecommendService:

    async def get_recommendations(
        self, films: List[FilmShortModel]
    ) -> List[FilmShortModel]:

        seen_ids = {film.id for film in films}

        count: Dict = Counter(genre.name for film in films for genre in film.genres)
        top_genres = [gnr[0] for gnr in count.most_common(2)]

        if not top_genres:
            return []

        query_params = "&".join([f"genres.name={genre}" for genre in top_genres])

        url = f"https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&{query_params}"

        headers = {"X-API-KEY": Config.KINOPOISK_API_KEY}

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)

        films_data: List[dict] = response.json()["docs"]

        filtered_films = [film for film in films_data if film["id"] not in seen_ids]

        filtered_films.sort(key=lambda x: x["rating"]["kp"], reverse=True)

        recommendations = [
            FilmShortModel(
                id=film["id"],
                title=film.get("name") or film.get("alternativeName") or film.get("enName") or "Неизвестно",
                year=film["year"],
                genres=film["genres"],
                poster=film.get("poster", {}).get("url", ""),
                status=FilmStatus.PLANNED
            )
            for film in filtered_films
        ]

        return recommendations
