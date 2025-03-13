from fastapi import FastAPI

from .routes import recommendRouter


app = FastAPI()

app.include_router(
    recommendRouter,
    prefix="/recommend",
    tags=["recommendations"])
