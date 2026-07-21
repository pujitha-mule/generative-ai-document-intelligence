import json
import os
from io import BytesIO

from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException
from openai import OpenAI
from pydantic import BaseModel
from pypdf import PdfReader

load_dotenv()

app = FastAPI(title="Generative AI Document Intelligence System", version="1.0.0")

class ExtractedDocument(BaseModel):
    name: str | None = None
    date: str | None = None
    amount: str | None = None
    category: str | None = None
    summary: str | None = None

def extract_pdf_text(raw: bytes) -> str:
    reader = PdfReader(BytesIO(raw))
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def get_client() -> OpenAI:
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY is not configured.")
    return OpenAI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/extract", response_model=ExtractedDocument)
async def extract_document(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    raw = await file.read()
    text = extract_pdf_text(raw).strip()

    if not text:
        raise HTTPException(
            status_code=422,
            detail="No machine-readable text found. Scanned PDFs require OCR."
        )

    prompt = f"""Extract the following five fields from this document:
name, date, amount, category, summary.

Rules:
- Return valid JSON only.
- Use null when a field is unavailable.
- category should be a short document/category label.
- summary should be concise.

Document:
{text[:20000]}
"""

    client = get_client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You extract structured information from documents."},
            {"role": "user", "content": prompt},
        ],
    )

    data = json.loads(response.choices[0].message.content)
    return ExtractedDocument(**data)
