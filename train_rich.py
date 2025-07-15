# train_rich.py

import joblib
from sklearn.ensemble import GradientBoostingClassifier

# 1. Load the rich pairs you just generated
X, y = joblib.load("data/rich_pairs.joblib")

# 2. Train a simple gradient‑boosting classifier
model = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)
model.fit(X, y)

# 3. Save the trained model
joblib.dump(model, "data/rich_match_model.joblib")
print("✅ Trained rich_match_model.joblib")
