from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.extractor import extract_text
from app.services.scorer import score_resume
from app.models.response import ATSScoreResponse

router = APIRouter()

@router.post("/analyze", response_model=ATSScoreResponse)
async def analyze_resume(file: UploadFile = File(...)):
    try:
        text = extract_text(file)
        scoring = score_resume(text)

        return ATSScoreResponse(
            filename=file.filename,
            detected_role=scoring["detected_role"],
            score=scoring["score"],
            missing_keywords=scoring["missing_keywords"],
            suggestions=scoring["suggestions"],
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
