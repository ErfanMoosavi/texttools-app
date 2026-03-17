from openai import AsyncOpenAI

from texttools import AsyncTheTool

from .config import settings

client = AsyncOpenAI(api_key=settings.api_key, base_url=settings.base_url)
tool = AsyncTheTool(client=client, model=settings.llm_model)

def get_tool() -> AsyncTheTool:
    return tool
