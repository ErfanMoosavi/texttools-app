from fastapi import APIRouter, HTTPException, status
from openai import OpenAI
from .schemas import Config, ProcessRequest
from texttools.models import ToolOutput

from texttools import TheTool

router = APIRouter()
tool = None


@router.post("/configuration", status_code=status.HTTP_201_CREATED)
def create_config(config: Config):
    try:
        client = OpenAI(api_key=config.api_key, base_url=config.base_url)
        global tool
        tool = TheTool(client=client, model=config.model)
        return {"message": "Created TheTool successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/process", status_code=status.HTTP_200_OK)
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
