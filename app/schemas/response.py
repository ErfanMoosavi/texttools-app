from pydantic import BaseModel


class StrRes(BaseModel):
    result: str


class BoolRes(BaseModel):
    result: bool


class ListStrRes(BaseModel):
    result: list[str]


class ListDictRes(BaseModel):
    result: list[dict[str, str]]
