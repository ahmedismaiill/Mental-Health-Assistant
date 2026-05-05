from fastapi import FastAPI
from .api.routes import router

app = FastAPI(title="Mental Health API")

# Register all routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running"}