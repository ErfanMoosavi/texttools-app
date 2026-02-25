from contextlib import asynccontextmanager

from fastapi import FastAPI

from .config import settings
from .routes import tool_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown


app = FastAPI(
    title=settings.title,
    version=settings.version,
    description=settings.description,
    contact=settings.contact,
    license_info=settings.license_info,
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {"message": "Welcome to TextTools API", "version": settings.version}


app.include_router(tool_routes)
