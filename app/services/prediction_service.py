from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "artifacts" / "churn_pipeline.joblib"

model_pipeline = joblib.load(MODEL_PATH)

def predict_churn(customer_data: dict):

    input_data = pd.DataFrame([customer_data])

    churn_probability = model_pipeline.predict_proba(
        input_data
    )[0][1]

    threshold = 0.35

    prediction = int(
        churn_probability >= threshold
    )

    return prediction, churn_probability