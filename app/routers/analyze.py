from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.extractor import extract_text
from app.models.response import AnalyzeResponse

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_resume(file: UploadFile = File(...)):
    try:
        text = extract_text(file)
        return AnalyzeResponse(
            filename=file.filename,
            text_length=len(text)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
