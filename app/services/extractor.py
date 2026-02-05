import pdfplumber
from docx import Document
from fastapi import UploadFile

def extract_text(file: UploadFile) -> str:
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        return _extract_pdf(file)
    elif filename.endswith(".docx"):
        return _extract_docx(file)
    else:
        raise ValueError("Unsupported file type")


def _extract_pdf(file: UploadFile) -> str:
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def _extract_docx(file: UploadFile) -> str:
    document = Document(file.file)
    return "\n".join([para.text for para in document.paragraphs])
