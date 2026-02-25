from pydantic import BaseModel
from texttools.models import ToolOutput


class ToolRes(BaseModel):
    output: ToolOutput
