from fastapi import APIRouter

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
async def categorize(req: CategorizeReq):
    pass


@router.post("/extract_keywords")
async def extract_keywords(req: ExtractKeywordsReq):
    pass


@router.post("/extract_entities")
async def extract_entities(req: ExtractEntitiesReq):
    pass


@router.post("/is_question")
async def is_question(req: IsQuestionReq):
    pass


@router.post("/to_question")
async def to_question(req: ToQuestionReq):
    pass


@router.post("/merge_questions")
async def merge_questions(req: MergeQuestionsReq):
    pass


@router.post("/augment")
async def augment(req: AugmentReq):
    pass


@router.post("/summarize")
async def summarize(req: SummarizeReq):
    pass


@router.post("/translate")
async def translate(req: TranslateReq):
    pass


@router.post("/propositionize")
async def propositionize(req: PropositionizeReq):
    pass


@router.post("/is_fact")
async def is_fact(req: IsFactReq):
    pass
