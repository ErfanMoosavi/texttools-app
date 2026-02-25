from fastapi import APIRouter, Depends

from texttools import AsyncTheTool

from ..dependencies import get_tool
from ..schemas import (
    AugmentReq,
    CategorizeReq,
    ExtractEntitiesReq,
    ExtractKeywordsReq,
    IsFactReq,
    IsQuestionReq,
    MergeQuestionsReq,
    PropositionizeReq,
    SummarizeReq,
    ToQuestionReq,
    TranslateReq,
)

router = APIRouter(prefix="/tools", tags=["tools"])


@router.post("/categorize")
async def categorize(req: CategorizeReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.categorize(
        text=req.text,
        categories=req.categories,
        with_analysis=req.with_analysis,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return result


@router.post("/extract_keywords")
async def extract_keywords(
    req: ExtractKeywordsReq, tool: AsyncTheTool = Depends(get_tool)
):
    result = await tool.extract_keywords(
        text=req.text,
        mode=req.mode,
        number_of_keywords=req.number_of_keywords,
        with_analysis=req.with_analysis,
        output_lang=req.output_lang,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return result


@router.post("/extract_entities")
async def extract_entities(
    req: ExtractEntitiesReq, tool: AsyncTheTool = Depends(get_tool)
):
    result = await tool.extract_entities(
        text=req.text,
        entities=req.entities,
        with_analysis=req.with_analysis,
        output_lang=req.output_lang,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return result


@router.post("/is_question")
async def is_question(req: IsQuestionReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.is_question(
        text=req.text,
        with_analysis=req.with_analysis,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return result


@router.post("/to_question")
async def to_question(req: ToQuestionReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.to_question(
        text=req.text,
        number_of_questions=req.number_of_questions,
        mode=req.mode,
        with_analysis=req.with_analysis,
        output_lang=req.output_lang,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return result


@router.post("/merge_questions")
async def merge_questions(
    req: MergeQuestionsReq, tool: AsyncTheTool = Depends(get_tool)
):
    result = await tool.merge_questions(
        text=req.text,
        mode=req.mode,
        with_analysis=req.with_analysis,
        output_lang=req.output_lang,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return result


@router.post("/augment")
async def augment(req: AugmentReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.augment(
        text=req.text,
        mode=req.mode,
        with_analysis=req.with_analysis,
        output_lang=req.output_lang,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return result


@router.post("/summarize")
async def summarize(req: SummarizeReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.summarize(
        text=req.text,
        with_analysis=req.with_analysis,
        output_lang=req.output_lang,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return result


@router.post("/translate")
async def translate(req: TranslateReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.translate(
        text=req.text,
        target_language=req.target_language,
        use_chunker=req.use_chunker,
        max_concurrent_chunks=req.max_concurrent_chunks,
        with_analysis=req.with_analysis,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return result


@router.post("/propositionize")
async def propositionize(
    req: PropositionizeReq, tool: AsyncTheTool = Depends(get_tool)
):
    result = await tool.propositionize(
        text=req.text,
        with_analysis=req.with_analysis,
        output_lang=req.output_lang,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return result


@router.post("/is_fact")
async def is_fact(req: IsFactReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.is_fact(
        text=req.text,
        source_text=req.source_text,
        with_analysis=req.with_analysis,
        output_lang=req.output_lang,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return result
