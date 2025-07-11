# generate_mock_data.py
import random, itertools, joblib, numpy as np
from vectorizer import vectorize, LOVE_LANGS, HOBBIES

NUM_USERS = 200
COS_THRESHOLD = 0.55
RNG = random.Random(42)


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


users_json = [random_user() for _ in range(NUM_USERS)]
users_vec  = [vectorize(u) for u in users_json]


pairs_features = []
labels         = []

for i, j in itertools.combinations(range(NUM_USERS), 2):
    vecA, vecB = users_vec[i], users_vec[j]


    diff = np.abs(vecA - vecB)
    cos  = np.dot(vecA, vecB) / (np.linalg.norm(vecA) * np.linalg.norm(vecB))
    feature = np.hstack([diff, cos])
    pairs_features.append(feature)

    cos = float(np.dot(vecA, vecB) / (np.linalg.norm(vecA) * np.linalg.norm(vecB)))
    labels.append(1 if cos > COS_THRESHOLD else 0)

pairs_features = np.stack(pairs_features).astype(np.float32)
labels         = np.array(labels, dtype=np.int8)

print("Generated:", pairs_features.shape[0], "pairs")
print("Positive matches:", int(labels.sum()))

joblib.dump((pairs_features, labels), "pairs_labels.joblib")
print("Saved to pairs_labels.joblib")
