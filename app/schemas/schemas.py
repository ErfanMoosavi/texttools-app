from pydantic import BaseModel, Field
from typing import Literal


class BaseToolReq(BaseModel):
    text: str = Field(..., description="The input text")
    with_analysis: bool = Field(
        False, description="Add a reasoning step before generating the final output"
    )
    user_prompt: str | None = Field(None, description="Additional instructions")
    temperature: float = Field(0.0, description="Controls randomness", ge=0.0, le=2.0)


class BaseToolWithLangReq(BaseToolReq):
    output_lang: str | None = Field(
        None, description="Force the model to respond in a specific language"
    )


class CategorizeReq(BaseToolReq):
    categories: list[str] = Field(..., description="Category list")


class ExtractKeywordsReq(BaseToolWithLangReq):
    mode: Literal["auto", "threshold", "count"] = Field(
        "auto", description="Mode for keyword extraction"
    )
    number_of_keywords: int | None = Field(
        None, description="Number of keywords (required when mode='count')"
    )


class ExtractEntitiesReq(BaseToolWithLangReq):
    entities: list[str] = Field(
        ["all named entities"], description="list of entity types to extract"
    )


class IsQuestionReq(BaseToolReq):
    pass


class ToQuestionReq(BaseToolWithLangReq):
    number_of_questions: int = Field(
        1, description="Number of questions to generate", ge=1
    )
    mode: Literal["from_text", "from_subject"] = Field(
        "from_text", description="Question generation mode"
    )


class MergeQuestionsReq(BaseModel):
    text: list[str] = Field(..., description="list of questions to merge")
    mode: Literal["simple", "stepwise"] = Field("simple", description="Merging mode")
    with_analysis: bool = Field(
        False, description="Add a reasoning step before generating the final output"
    )
    output_lang: str | None = Field(
        None, description="Force the model to respond in a specific language"
    )
    user_prompt: str | None = Field(None, description="Additional instructions")
    temperature: float = Field(0.0, description="Controls randomness", ge=0.0, le=2.0)


class AugmentReq(BaseToolWithLangReq):
    mode: Literal["positive", "negative", "hard_negative"] = Field(
        "positive", description="Augmentation mode"
    )


class SummarizeReq(BaseToolWithLangReq):
    pass


class TranslateReq(BaseToolReq):
    target_language: str = Field(..., description="Target language for translation")
    use_chunker: bool = Field(
        True, description="Whether to use text chunker for large texts"
    )
    max_concurrent_chunks: int = Field(
        5, description="Maximum number of chunks to process in parallel", ge=1
    )


class PropositionizeReq(BaseToolWithLangReq):
    pass


class IsFactReq(BaseToolWithLangReq):
    source_text: str = Field(..., description="Source text to check against")
