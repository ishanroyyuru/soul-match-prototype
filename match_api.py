# match_api.py

import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from feature_builder import encode_user, build_pair_features

app = FastAPI(title="SOUL Match API", version="0.8")

# Load your regressor
model = joblib.load("data/regressor_model.joblib")

class Profile(BaseModel):
    soulprint: dict
    values_and_ideals: dict

@app.post("/similarity")
def similarity(a: Profile, b: Profile):
    # 1) Build feature vector
    a_enc = encode_user(a.dict())
    b_enc = encode_user(b.dict())
    feat, label = build_pair_features(a_enc, b_enc)
    if feat is None:
        return {"score": 0.0}

    # 2) Predict a continuous score
    score = float(model.predict(feat.reshape(1, -1))[0])

    # 3) Clamp to [0,1]
    score = max(0.0, min(1.0, score))
    return {"score": score}
