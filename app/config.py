import os
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:YOUR_LOCAL_PASSWORD@localhost:3306/customer_churn_db"
)