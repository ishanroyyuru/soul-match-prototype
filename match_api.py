# match_api.py
import numpy as np
from numpy.linalg import norm
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from vectorizer import vectorize  

class Profile(BaseModel):
    openness: float
    conscientiousness: float
    extroversion: float
    agreeableness: float
    neuroticism: float
    love_languages: list[str]
    hobbies: list[str]

model = joblib.load("match_model.joblib")

app = FastAPI(title="SOUL Match API", version="0.1")

@app.post("/similarity")
def similarity(a: Profile, b: Profile):
    vecA, vecB = vectorize(a.dict()), vectorize(b.dict())

    diff = abs(vecA - vecB)

    cos  = np.dot(vecA, vecB) / (norm(vecA) * norm(vecB))

    feature = np.hstack([diff, cos]).reshape(1, -1)

    score = float(model.predict_proba(feature)[0, 1])
    return {"score": score}
