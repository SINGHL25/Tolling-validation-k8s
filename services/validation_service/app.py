from fastapi import FastAPI
from pydantic import BaseModel
import json
import os
from typing import Optional


app = FastAPI(title="Validation Service")
DB_PATH = os.path.join('db')


def load_db(name):
try:
with open(os.path.join(DB_PATH, name), 'r') as f:
return json.load(f)
except Exception:
return []


GOLDEN = load_db('golden_vehicles.json')
SILVER = load_db('silver_vehicles.json')


class ValReq(BaseModel):
plate: str
confidence: Optional[float] = 0.0


@app.post("/validate")
def validate(req: ValReq):
plate = req.plate.strip().upper()
# exact match golden
for r in GOLDEN:
if r.get('plate').upper() == plate:
return {"plate": plate, "match":"golden", "owner": r.get('owner'), "type": r.get('type')}
# exact match silver
for r in SILVER:
if r.get('plate').upper() == plate:
return {"plate": plate, "match":"silver", "owner": r.get('owner'), "type": r.get('type')}
# no match
return {"plate": plate, "match":"none"}


@app.get("/")
def root():
return {"msg":"Validation service up"}
