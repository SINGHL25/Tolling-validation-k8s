from fastapi import FastAPI, File, UploadFile, Form
import requests
import os
import uuid
from pydantic import BaseModel


app = FastAPI(title="Image Ingestion Service")
OCR_URL = os.getenv('OCR_URL','http://localhost:8001/ocr')


class IngestResult(BaseModel):
id: str
plate: str
confidence: float
ocr_raw: dict


@app.post("/ingest")
async def ingest(file: UploadFile = File(None), plate_text: str = Form(None)):
"""
Accepts an image upload or plate text (for demo). If plate_text is provided, sends to OCR endpoint as input.
Returns combined OCR result and id.
"""
# For demo, if plate_text is provided use it, else pretend to upload and ask OCR to analyze
payload = {"plate_text": plate_text} if plate_text else None
try:
resp = requests.post(OCR_URL, json=payload, timeout=5)
resp.raise_for_status()
ocr = resp.json()
except Exception as e:
ocr = {"plate": plate_text or "UNKNOWN", "confidence": 0.0, "error": str(e)}
# generate an id
uid = str(uuid.uuid4())
# forward to validation service (optional)
return {"id": uid, "plate": ocr.get('plate'), "confidence": ocr.get('confidence'), "ocr_raw": ocr}


@app.get("/")
async def root():
return {"msg":"Image Ingestion Service up. POST /ingest"}
