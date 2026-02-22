from typing import Literal

from pydantic import BaseModel


class Config(BaseModel):
    api_key: str
    base_url: str
    model: str


class ProcessRequest(BaseModel):
    operation: Literal[
        "extract_keywords", "extract_entities", "is_question", "to_question"
    ]
    text: str
