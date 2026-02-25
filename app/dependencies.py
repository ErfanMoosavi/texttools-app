from openai import AsyncOpenAI

from texttools import AsyncTheTool

from .config import settings


def get_tool() -> AsyncTheTool:
    client = AsyncOpenAI(api_key=settings.api_key, base_url=settings.base_url)
    return AsyncTheTool(client=client, model=settings.llm_model)
