import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score
)

from preprocessing import preprocessor


DATA_PATH = "data/customer_churn_cleaned.csv"

# Load data
df = pd.read_csv(DATA_PATH)

X = df.drop("Churn", axis=1)
y = df["Churn"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

# Create pipeline
model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(
            max_iter=1000
        ))
    ]
)

# Train
model_pipeline.fit(X_train, y_train)

# Get probability of churn
churn_probability = model_pipeline.predict_proba(X_test)[:, 1]


# Test different thresholds
thresholds = [0.30, 0.35, 0.40, 0.45, 0.50]

print("\n===== THRESHOLD ANALYSIS =====")

for threshold in thresholds:

    y_pred = (
        churn_probability >= threshold
    ).astype(int)

    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"\nThreshold: {threshold}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")