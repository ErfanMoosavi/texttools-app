from texttools import AsyncTheTool
from openai import OpenAI

from .config import settings


def get_tool() -> AsyncTheTool:
    client = OpenAI(api_key=settings.api_key, base_url=settings.base_url)
    return AsyncTheTool(client=client, model=settings.llm_model)
