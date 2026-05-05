from fastapi import FastAPI
from backend.rag_app.api.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Mental Health Assistant API is running"}