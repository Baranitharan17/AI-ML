import re
import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# Load datasets
train = pd.read_csv("data/processed/train.csv")
val = pd.read_csv("data/processed/validation.csv")

# Remove artificial ticket reference
def clean_text(text):
    text = str(text).lower().strip()
    text = re.sub(
        r"\s*-\s*ticket reference\s+[a-z]+-\d+\s*$",
        "", text
    )
    return text.strip()

X_train = train["text"].apply(clean_text)
X_val = val["text"].apply(clean_text)

# Hyperparameter tuning
params = {
    "tfidf__ngram_range": [(1, 1), (1, 2)],
    "classifier__C": [0.1, 1, 10]
}

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

def build_model(target):

    y_train = train[target]
    y_val = val[target]

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("classifier", LogisticRegression(max_iter=2000))
    ])

    grid = GridSearchCV(
        pipeline,
        params,
        cv=cv,
        scoring="f1_macro",
        n_jobs=-1
    )

    grid.fit(X_train, y_train)

    model = grid.best_estimator_
    predictions = model.predict(X_val)

    print("\nTarget:", target)
    print("Best parameters:", grid.best_params_)

    print("Accuracy:",
          accuracy_score(y_val, predictions))

    print("Macro F1:",
          f1_score(y_val, predictions, average="macro"))

    print("\nClassification Report:")
    print(classification_report(y_val, predictions))

    print("Confusion Matrix:")
    print(confusion_matrix(y_val, predictions))

    return model

# Train category model
category_model = build_model("category")

# Train priority model
priority_model = build_model("priority")

# Save models
import os
os.makedirs("models", exist_ok=True)

joblib.dump(
    category_model,
    "models/category_baseline.joblib"
)

joblib.dump(
    priority_model,
    "models/priority_baseline.joblib"
)

print("\nBoth baseline models saved successfully!")
