from fastapi import FastAPI, status
from openai import OpenAI
from texttools.models import ToolOutput

from texttools import TheTool

from backend.schemas import Config, ProcessRequest

app = FastAPI(
    title="TextTools App",
    description="A FastAPI web app for texttools",
    license_info={"name": "MIT"},
    version="0.1.0",
)


tool = None


@app.post("/configuration", status_code=status.HTTP_201_CREATED)
def create_config(config: Config):
    client = OpenAI(api_key=config.api_key, base_url=config.base_url)
    global tool
    tool = TheTool(client=client, model=config.model)
    return {"message": "Created TheTool successfully"}


@app.post("/process", status_code=status.HTTP_200_OK)
def process(request: ProcessRequest) -> ToolOutput:
    method = getattr(tool, request.operation)
    output = method(request.text)
    return output
