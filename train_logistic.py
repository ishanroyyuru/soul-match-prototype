# train_logistic.py

import joblib
from sklearn.linear_model import LogisticRegression

# 1) Load your rich feature dataset
X, y = joblib.load("data/rich_pairs.joblib")

# 2) Train a logistic model
clf = LogisticRegression(max_iter=1000, random_state=42)
clf.fit(X, y)

# 3) Save it
joblib.dump(clf, "data/logistic_model.joblib")
print("Saved data/logistic_model.joblib")
