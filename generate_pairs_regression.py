# generate_pairs_regression.py

import itertools, joblib, json, numpy as np
from feature_builder import encode_user, build_pair_features

# Load your mock profiles
profiles = json.load(open("mock_profiles.json"))

X, y = [], []
for a, b in itertools.combinations(profiles, 2):
    a_enc = encode_user(a)
    b_enc = encode_user(b)
    feat, label = build_pair_features(a_enc, b_enc)
    if feat is None:
        continue
    X.append(feat)
    # label = the raw average of the four features
    y.append(float(feat.mean()))

X = np.stack(X).astype(np.float32)
y = np.array(y, dtype=np.float32)

joblib.dump((X, y), "data/regression_pairs.joblib")
print(f"Saved {len(y)} regression pairs.")
