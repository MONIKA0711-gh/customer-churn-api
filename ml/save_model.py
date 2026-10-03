import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from preprocessing import preprocessor


DATA_PATH = "data/customer_churn_cleaned.csv"
MODEL_PATH = "../artifacts/churn_pipeline.joblib"


# Load data
df = pd.read_csv(DATA_PATH)

X = df.drop("Churn", axis=1)
y = df["Churn"]


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)


# Create final pipeline
model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(
            max_iter=1000
        ))
    ]
)


# Train on training data
model_pipeline.fit(X_train, y_train)


# Save complete pipeline
joblib.dump(
    model_pipeline,
    MODEL_PATH
)

print("Model saved successfully!")
print(f"Saved to: {MODEL_PATH}")