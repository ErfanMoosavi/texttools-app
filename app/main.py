from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
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

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/categorize")
async def categorize_page(request: Request):
    return templates.TemplateResponse("categorize.html", {"request": request})


@app.get("/extract-keywords")
async def extract_keywords_page(request: Request):
    return templates.TemplateResponse("extract_keywords.html", {"request": request})


@app.get("/extract-entities")
async def extract_entities_page(request: Request):
    return templates.TemplateResponse("extract_entities.html", {"request": request})


@app.get("/is-question")
async def is_question_page(request: Request):
    return templates.TemplateResponse("is_question.html", {"request": request})


@app.get("/to-question")
async def to_question_page(request: Request):
    return templates.TemplateResponse("to_question.html", {"request": request})


@app.get("/merge-questions")
async def merge_questions_page(request: Request):
    return templates.TemplateResponse("merge_questions.html", {"request": request})


@app.get("/augment")
async def augment_page(request: Request):
    return templates.TemplateResponse("augment.html", {"request": request})


@app.get("/summarize")
async def summarize_page(request: Request):
    return templates.TemplateResponse("summarize.html", {"request": request})


@app.get("/translate")
async def translate_page(request: Request):
    return templates.TemplateResponse("translate.html", {"request": request})


@app.get("/propositionize")
async def propositionize_page(request: Request):
    return templates.TemplateResponse("propositionize.html", {"request": request})


@app.get("/fact-check")
async def fact_check_page(request: Request):
    return templates.TemplateResponse("fact_check.html", {"request": request})


app.include_router(tool_routes)
