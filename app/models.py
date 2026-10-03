from sqlalchemy import Column, Integer, Float, String

from app.database import Base


class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    gender = Column(
        String(20)
    )

    tenure = Column(
        Integer
    )

    contract = Column(
        String(50)
    )

    monthly_charges = Column(
        Float
    )

    total_charges = Column(
        Float
    )

    churn_prediction = Column(
        Integer
    )

    churn_probability = Column(
        Float
    )

    # Additional customer features

    internet_service = Column(
        String(30)
    )

    online_security = Column(
        String(30)
    )

    tech_support = Column(
        String(30)
    )

    payment_method = Column(
        String(50)
    )

    paperless_billing = Column(
        String(10)
    )