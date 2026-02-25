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
    ToolRes,
    ToQuestionReq,
    TranslateReq,
)

router = APIRouter(prefix="/tools", tags=["tools"])


@router.post("/categorize", response_model=ToolRes)
async def categorize(req: CategorizeReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.categorize(
        text=req.text,
        categories=req.categories,
        with_analysis=req.with_analysis,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return ToolRes(output=result)


@router.post("/extract_keywords", response_model=ToolRes)
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
    return ToolRes(output=result)


@router.post("/extract_entities", response_model=ToolRes)
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
    return ToolRes(output=result)


@router.post("/is_question", response_model=ToolRes)
async def is_question(req: IsQuestionReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.is_question(
        text=req.text,
        with_analysis=req.with_analysis,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return ToolRes(output=result)


@router.post("/to_question", response_model=ToolRes)
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
    return ToolRes(output=result)


@router.post("/merge_questions", response_model=ToolRes)
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
    return ToolRes(output=result)


@router.post("/augment", response_model=ToolRes)
async def augment(req: AugmentReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.augment(
        text=req.text,
        mode=req.mode,
        with_analysis=req.with_analysis,
        output_lang=req.output_lang,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return ToolRes(output=result)


@router.post("/summarize", response_model=ToolRes)
async def summarize(req: SummarizeReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.summarize(
        text=req.text,
        with_analysis=req.with_analysis,
        output_lang=req.output_lang,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return ToolRes(output=result)


@router.post("/translate", response_model=ToolRes)
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
    return ToolRes(output=result)


@router.post("/propositionize", response_model=ToolRes)
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
    return ToolRes(output=result)


@router.post("/is_fact", response_model=ToolRes)
async def is_fact(req: IsFactReq, tool: AsyncTheTool = Depends(get_tool)):
    result = await tool.is_fact(
        text=req.text,
        source_text=req.source_text,
        with_analysis=req.with_analysis,
        output_lang=req.output_lang,
        user_prompt=req.user_prompt,
        temperature=req.temperature,
    )
    return ToolRes(output=result)
