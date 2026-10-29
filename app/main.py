from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.user_model import User
from sqlalchemy.orm import Session
from app.auth_routes import router as auth_router

from app.auth import get_current_user

from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse
)

from app.services.prediction_service import predict_churn

from app.database import (
    Base,
    engine,
    get_db
)

from app.models import Prediction


# =====================================================
# Create Database Tables
# =====================================================

Base.metadata.create_all(bind=engine)


# =====================================================
# FastAPI Application
# =====================================================

app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn using machine learning",
    version="1.0.0"
)

app.include_router(auth_router)


# =====================================================
# CORS Configuration
# =====================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# =====================================================
# Root Endpoint
# =====================================================

@app.get("/")
def root():

    return {
        "message": "Customer Churn Prediction API is running"
    }


# =====================================================
# Health Check
# =====================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


# =====================================================
# Predict Churn
# =====================================================

@app.post(
    "/predict-churn",
    response_model=PredictionResponse
)
def predict(
    request: PredictionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Convert request into dictionary
    customer_data = request.model_dump()

    # Get ML prediction
    prediction, probability = predict_churn(
        customer_data
    )

    # Determine result
    if prediction == 1:

        result = "Customer is likely to churn"

    else:

        result = "Customer is unlikely to churn"


    # =================================================
    # Save Prediction to MySQL
    # =================================================

    db_prediction = Prediction(

        gender=request.gender,

        tenure=request.tenure,

        contract=request.Contract,

        monthly_charges=request.MonthlyCharges,

        total_charges=request.TotalCharges,

        churn_prediction=prediction,

        churn_probability=probability,

        internet_service=request.InternetService,

        online_security=request.OnlineSecurity,

        tech_support=request.TechSupport,

        payment_method=request.PaymentMethod,

        user_id = current_user.id,

        paperless_billing=request.PaperlessBilling
    )


    db.add(db_prediction)

    db.commit()

    db.refresh(db_prediction)


    # =================================================
    # Return Prediction
    # =================================================

    return {

        "churn_prediction": prediction,

        "churn_probability":
            round(probability, 4),

        "result": result
    }


# =====================================================
# Prediction History
# =====================================================

@app.get("/predictions")
def get_predictions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    predictions = (
        db.query(Prediction)
        .filter(Prediction.user_id == current_user.id)
        .order_by(Prediction.id.asc())
        .all()
    )

    return [
        {
            "id": prediction.id,
            "gender": prediction.gender,
            "tenure": prediction.tenure,
            "contract": prediction.contract,
            "monthly_charges": prediction.monthly_charges,
            "total_charges": prediction.total_charges,
            "churn_prediction": prediction.churn_prediction,
            "churn_probability": prediction.churn_probability,
            "internet_service": prediction.internet_service,
            "online_security": prediction.online_security,
            "tech_support": prediction.tech_support,
            "payment_method": prediction.payment_method,
            "paperless_billing": prediction.paperless_billing
        }
        for prediction in predictions
    ]