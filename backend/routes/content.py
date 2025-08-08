from fastapi import APIRouter, Request
from pydantic import BaseModel
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

router = APIRouter()

class QARequest(BaseModel):
    context: str
    question: str

@router.post("/qa")
async def answer_question(data: QARequest):
    result = qa_pipeline({
        "context": data.context,
        "question": data.question
    })
    return {"answer": result["answer"]}
