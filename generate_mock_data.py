# generate_mock_data.py
import random, itertools, joblib, numpy as np
from vectorizer import vectorize, LOVE_LANGS, HOBBIES

NUM_USERS = 200
COS_THRESHOLD = 0.75         # >0.75 → label 1, else 0
RNG = random.Random(42)      # reproducible

# ----- helper to create one fake user -----
def random_user() -> dict:
    return {
        "openness": round(RNG.random(), 2),
        "conscientiousness": round(RNG.random(), 2),
        "extroversion": round(RNG.random(), 2),
        "agreeableness": round(RNG.random(), 2),
        "neuroticism": round(RNG.random(), 2),
        "love_languages": RNG.sample(LOVE_LANGS, k=2),
        "hobbies": RNG.sample(HOBBIES, k=3),
    }

# ----- 1. generate users -----
users_json = [random_user() for _ in range(NUM_USERS)]
users_vec  = [vectorize(u) for u in users_json]

# ----- 2. create all unique pairs -----
pairs_features = []
labels         = []

for i, j in itertools.combinations(range(NUM_USERS), 2):
    vecA, vecB = users_vec[i], users_vec[j]

    # pair feature: absolute diff
    feature = np.abs(vecA - vecB)
    pairs_features.append(feature)

    # dummy label based on cosine similarity
    cos = float(np.dot(vecA, vecB) / (np.linalg.norm(vecA) * np.linalg.norm(vecB)))
    labels.append(1 if cos > COS_THRESHOLD else 0)

pairs_features = np.stack(pairs_features).astype(np.float32)
labels         = np.array(labels, dtype=np.int8)

print("Generated:", pairs_features.shape[0], "pairs")
print("Positive matches:", int(labels.sum()))

# ----- 3. save to disk -----
joblib.dump((pairs_features, labels), "pairs_labels.joblib")
print("Saved to pairs_labels.joblib")
