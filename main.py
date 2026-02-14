from backend.routers import router
from fastapi import FastAPI

app = FastAPI(
    title="TextTools App",
    description="A FastAPI web app for texttools",
    license_info={"name": "MIT"},
    version="0.1.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Welcome to TextTools App"}
