# calibrate_model.py

import joblib
from sklearn.calibration       import CalibratedClassifierCV
from sklearn.linear_model     import LogisticRegression

# 1) Load your rich dataset and base model
X, y        = joblib.load("data/rich_pairs.joblib")
base_clf    = joblib.load("data/logistic_model.joblib")

# 2) Wrap it in a sigmoid‐based calibrator (using 5‑fold CV)
calibrated = CalibratedClassifierCV(base_clf, method="isotonic", cv=5)
calibrated.fit(X, y)

# 3) Save the calibrated version
joblib.dump(calibrated, "data/calibrated_model.joblib")
print("✅ Saved data/calibrated_model.joblib")
