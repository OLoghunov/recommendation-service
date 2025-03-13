from fastapi import FastAPI

from .routes import recommend_router


app = FastAPI()

app.include_router(
    recommend_router,
    prefix="/recommend",
    tags=["recommendations"])
