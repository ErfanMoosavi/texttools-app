from fastapi import FastAPI

from .config import settings
from .routers import tool_routes


app = FastAPI(
    title=settings.title,
    version=settings.version,
    description=settings.description,
    contact=settings.contact,
    license_info=settings.license_info,
)

app.include_router(tool_routes)
