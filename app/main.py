from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

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

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(jinja2_req: Request):
    return templates.TemplateResponse(jinja2_req, "home.html")


app.include_router(tool_routes)
