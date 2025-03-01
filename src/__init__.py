from fastapi import FastAPI

app = FastAPI()

@app.get("/recommendations/{user_id}")
async def get_recommendations(user_id: int):

    return {"user_id": user_id, "recommendations": ["Film 1", "Film 2", "Film 3"]}
