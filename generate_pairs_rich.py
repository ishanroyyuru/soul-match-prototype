# generate_pairs_rich.py (modified)

import itertools, joblib, json, numpy as np
from feature_builder import encode_user, build_pair_features

# threshold for calling a pair “compatible”
POS_THRESHOLD = 0.50

profiles = json.load(open("mock_profiles.json"))

X, y = [], []
for a, b in itertools.combinations(profiles, 2):
    a_enc = encode_user(a)
    b_enc = encode_user(b)
    feat, hard_label = build_pair_features(a_enc, b_enc)

    if feat is None:
        continue

    # compute synthetic label:
    # average of [mbti, ennea, attach, love] > POS_THRESHOLD → 1, else 0
    avg_score = float(feat.mean())
    label = 1 if avg_score > POS_THRESHOLD else 0

    X.append(feat)
    y.append(label)

X = np.stack(X).astype(np.float32)
y = np.array(y, dtype=np.int8)
joblib.dump((X, y), "data/rich_pairs.joblib")
print(f"Saved {X.shape[0]} pairs ({y.sum()} positives) to data/rich_pairs.joblib")
