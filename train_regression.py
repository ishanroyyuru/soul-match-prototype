# train_regressor.py

import joblib
from sklearn.ensemble import GradientBoostingRegressor

# 1) Load regression pairs
X, y = joblib.load("data/regression_pairs.joblib")

# 2) Train a GB regressor
reg = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=5, random_state=42)
reg.fit(X, y)

# 3) Save it
joblib.dump(reg, "data/regressor_model.joblib")
print("Saved data/regressor_model.joblib")
