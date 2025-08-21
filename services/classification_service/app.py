from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os


app = FastAPI(title="Classification Service")
VALIDATION_URL = os.getenv('VALIDATION_URL','http://validation_service:80/validate')


class ClassReq(BaseModel):
plate: str
confidence: float


@app.post("/classify")
def classify(req: ClassReq):
# call validation
try:
resp = requests.post(VALIDATION_URL, json={"plate": req.plate, "confidence": req.confidence}, timeout=5)
data = resp.json()
except Exception as e:
return {"status":"error","error": str(e)}


match = data.get('match')
confidence = req.confidence
decision = 'manual'
reason = ''
# simple decision logic
if match == 'golden' and confidence >= 85:
decision = 'auto-validated'
elif match in ('golden','silver') and confidence >= 70:
decision = 'semi-auto'
else:
decision = 'manual'
return {"plate": req.plate, "validation": data, "decision": decision}


@app.get('/')
def root():
return {"msg":"Classification service up"}
