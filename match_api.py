# match_api.py

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from feature_builder import encode_user, build_pair_features

app = FastAPI(title="SOUL Match API", version="0.4")

class Profile(BaseModel):
    soulprint: dict
    values_and_ideals: dict

@app.post("/similarity")
def similarity(a: Profile, b: Profile):
    # 1) Turn JSON into feature vector
    a_enc = encode_user(a.dict())
    b_enc = encode_user(b.dict())
    feat, label = build_pair_features(a_enc, b_enc)
    if feat is None:
        return {"score": 0.0}

    # 2) Pure weighted average of the four features:
    #    40% MBTI, 30% Enneagram, 20% Attachment, 10% Love-language overlap
    weights = np.array([0.4, 0.3, 0.2, 0.1], dtype=np.float32)
    score = float((feat * weights).sum() / weights.sum())

    # 3) Clamp just in case
    score = max(0.0, min(1.0, score))
    return {"score": score}
