import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from preprocessing import preprocessor


DATA_PATH = "data/customer_churn_cleaned.csv"


# Load cleaned dataset
df = pd.read_csv(DATA_PATH)

# Separate features and target
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


# Create ML pipeline
model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(
            max_iter=1000
        ))
    ]
)


# Train model
model_pipeline.fit(X_train, y_train)


print("Model training completed successfully!")

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))