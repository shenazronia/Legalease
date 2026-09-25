from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "LegalEase Backend is Running!"}
    app.include_router(router)
