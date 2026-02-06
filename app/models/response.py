from pydantic import BaseModel
from typing import List

class AnalyzeResponse(BaseModel):
    filename: str
    text_length: int

class ATSScoreResponse(BaseModel):
    filename: str
    detected_role: str
    score: int
    missing_keywords: List[str]
    suggestions: List[str]
