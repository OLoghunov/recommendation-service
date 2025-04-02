# Recommendation Service

## Description
`recommendation-service` is a microservice designed to generate movie recommendations for the main service [`pop-flix`](https://github.com/OLoghunov/pop-flix).

## Features
- Personalized movie recommendations based on user watch history.
- Filtering out already watched movies.
- Fetching movie data via the Kinopoisk API.
- Asynchronous interaction with the main service via REST API.

## Tech Stack
- **Language**: Python
- **Framework**: FastAPI
- **Containerization**: Docker, Docker Compose

## Installation & Running
### Local Setup (without Docker)
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

### Running with Docker
```bash
docker-compose up --build
```

## API
### Submit a List of Watched Movies and Get Recommendations
**POST** `/recommend/films`
#### Request Body:
```json
[
    {
        "id": 389,
        "title": "Леон",
        "year": 1994,
        "genres": [
            { "name": "боевик" },
            { "name": "триллер" },
            { "name": "драма" },
            { "name": "криминал" }
        ],
        "poster": "https://image.openmoviedb.com/kinopoisk-images/6201401/8662d92a-5881-4600-a7ae-549e6fd53b03/orig",
        "status": "watched",
        "tmdbId": 101
    },
    {
        "id": 397667,
        "title": "Остров проклятых",
        "year": 2009,
        "genres": [
            { "name": "триллер" },
            { "name": "детектив" },
            { "name": "драма" }
        ],
        "poster": "https://image.openmoviedb.com/kinopoisk-images/4303601/617303b7-cfa7-4273-bd1d-63974bf68927/orig",
        "status": "watched",
        "tmdbId": null
    }
]
```

#### Response:
```json
[
    {
        "id": 7334456,
        "title": "Мечты о прекрасном",
        "year": 2024,
        "genres": [
            {
                "name": "драма"
            }
        ],
        "poster": "https://image.openmoviedb.com/kinopoisk-images/10671298/6893518f-c726-4f80-b75e-71c61494536e/orig",
        "status": "planned",
        "tmdbId": null
    },
    {
        "id": 7331891,
        "title": "Heldin",
        "year": 2025,
        "genres": [
            {
                "name": "драма"
            }
        ],
        "poster": "",
        "status": "planned",
        "tmdbId": null
    }
]
```

## Integration with `pop-flix`
The microservice receives a list of watched movies from [`pop-flix`](https://github.com/OLoghunov/pop-flix) via a `POST` request to `/recommend/films`.

## License
This project is licensed under the MIT License.
