# train.py
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score, confusion_matrix

X, y = joblib.load("pairs_labels.joblib")   # X: (N, 20)  y: (N,)

print("Data loaded:", X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

probs = model.predict_proba(X_test)[:, 1]
preds = (probs > 0.5).astype(int)

auc  = roc_auc_score(y_test, probs)
acc  = accuracy_score(y_test, preds)
cm   = confusion_matrix(y_test, preds)

print(f"AUC  : {auc:.3f}")
print(f"Acc. : {acc:.3f}")
print("Confusion matrix:")
print(cm)

joblib.dump(model, "match_model.joblib")
print("Model saved to match_model.joblib")
