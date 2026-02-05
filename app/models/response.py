from pydantic import BaseModel

class AnalyzeResponse(BaseModel):
    filename: str
    text_length: int
