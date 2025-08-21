from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import random
import time
from fuzzywuzzy import fuzz


app = FastAPI(title="OCR Service")


class OCRRequest(BaseModel):
plate_text: Optional[str] = None


@app.post("/ocr")
def ocr(req: OCRRequest):
# Simulate OCR by returning the plate_text if provided, else fabricate
if req.plate_text:
plate = req.plate_text.strip().upper()
confidence = round(random.uniform(85, 99), 2)
else:
# fabricate plate
letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
numbers = ''.join(random.choices('0123456789', k=3))
plate = letters + numbers
confidence = round(random.uniform(60, 95), 2)
# simulate latency
time.sleep(random.uniform(0.1, 0.6))
return {"plate": plate, "confidence": confidence}


@app.get("/")
def root():
return {"msg":"OCR Service up"}
