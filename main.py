from fastapi import FastAPI, status, HTTPException
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
    try:
        client = OpenAI(api_key=config.api_key, base_url=config.base_url)
        global tool
        tool = TheTool(client=client, model=config.model)
        return {"message": "Created TheTool successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.post("/process", status_code=status.HTTP_200_OK)
def create_output(request: ProcessRequest) -> ToolOutput:
    if not tool:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Set configs first"
        )

    try:
        method = getattr(tool, request.operation)
        output = method(request.text)
        return output

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
