# 🔍 Customer Churn Prediction API

### Predict customer churn. Secure the data. Turn predictions into insights.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT"/>
</p>

<p align="center">
  <strong>A machine learning-powered REST API for customer churn prediction, with database persistence and JWT-based authentication.</strong>
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Why This Project?](#-why-this-project)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Configuration](#-environment-configuration)
- [API Documentation](#-api-documentation)
- [Security Implementation](#-security-implementation)
- [Database Design](#-database-design)
- [Testing the API](#-testing-the-api)
- [Future Improvements](#-future-improvements)
- [Learning Outcomes](#-learning-outcomes)

---

## 🎯 Overview

Customer Churn Prediction API is a Python backend application that predicts whether a customer is likely to stop using a company's products or services.

The application exposes a trained **Logistic Regression model** through FastAPI, allowing clients to submit customer information and receive predictions through REST API endpoints.

It also integrates MySQL for persistent prediction history and implements JWT-based authentication to protect endpoints and associate prediction records with individual users.

The project demonstrates how machine learning can be integrated into a secure, database-backed application rather than being used only as a standalone model.

## 💡 Why This Project?

Customer churn is a common challenge for businesses such as telecom providers, subscription platforms, and other service-based companies.

Losing customers can affect revenue and increase the cost of acquiring new customers. Predicting potential churn can help businesses identify customers who may need additional support or retention efforts.

This project demonstrates a technical approach to that problem by combining machine learning with backend application development.

**Main objective:** Build a secure and maintainable API that connects customer churn prediction, user authentication, and database-backed prediction history.

## ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 ML-based prediction | Uses a trained Logistic Regression model and preprocessing pipeline. |
| ⚡ REST API | Provides HTTP endpoints using FastAPI. |
| 🗄️ Database integration | Stores user accounts and prediction records in MySQL. |
| 🔐 User authentication | Supports registration, login, password hashing, and JWT access tokens. |
| 👤 User-specific history | Retrieves prediction records associated with the authenticated user. |
| ✅ Input validation | Uses Pydantic schemas to validate incoming data. |
| 📚 Interactive documentation | Provides API exploration and testing through Swagger UI. |
| 🧩 ORM integration | Uses SQLAlchemy to interact with the database through Python models. |
| ⚙️ Environment configuration | Keeps sensitive configuration outside the application source code. |

## 🔄 How It Works

The application follows an end-to-end prediction workflow.

1. **Register:** A new user creates an account.
2. **Authenticate:** The user logs in and receives a JWT access token.
3. **Submit data:** The client sends customer information to the prediction endpoint.
4. **Validate:** FastAPI validates the incoming request.
5. **Predict:** The trained machine learning pipeline processes the input and generates a churn prediction.
6. **Store:** The application saves the prediction and associated details in MySQL.
7. **Retrieve:** The authenticated user can access their own prediction history.

```mermaid
flowchart TD
    A[Client or API Consumer] --> B[User Registration and Login]
    B --> C[JWT Access Token]
    C --> D[FastAPI Backend]
    D --> E[Pydantic Validation]
    E --> F[Trained ML Pipeline]
    F --> G[Churn Prediction]
    G --> H[MySQL Database]
    H --> I[User-Specific Prediction History]
    I --> J[JSON API Response]
```

## 🏗️ System Architecture

The application is organized into separate layers.

- **API layer:** Receives HTTP requests and returns JSON responses.
- **Authentication layer:** Verifies JWT tokens and identifies the current user.
- **Machine learning layer:** Applies preprocessing and generates predictions.
- **Database layer:** Persists user and prediction records through SQLAlchemy.
- **Validation layer:** Checks request data using Pydantic schemas.

This separation makes the application easier to understand, test, and extend.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend framework and REST API development |
| Scikit-learn | Machine learning model and preprocessing pipeline |
| Logistic Regression | Customer churn classification |
| MySQL | Relational database |
| SQLAlchemy | ORM and database operations |
| Pydantic | Request and response validation |
| JWT | Token-based authentication |
| pwdlib | Password hashing and verification |
| Uvicorn | ASGI application server |
| Swagger UI | Interactive API documentation |
| Git and GitHub | Version control and source code management |

## 📂 Project Structure

```text
customer-churn-api/
│
├── app/
│   ├── main.py             # FastAPI application and endpoints
│   ├── auth.py             # Password hashing and JWT utilities
│   ├── auth_routes.py      # Registration and login endpoints
│   ├── config.py           # Environment-based configuration
│   ├── database.py         # SQLAlchemy engine and DB sessions
│   ├── models.py           # Prediction database model
│   ├── user_model.py       # User database model
│   └── schemas/
│       └── user.py         # User request/response schemas
│
├── ml/                     # Model training and preprocessing, if present
├── tests/                  # Automated tests, if present
├── .env.example            # Example environment configuration
├── .gitignore              # Files excluded from Git
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

> **Note:** Adjust the `ml/` and `tests/` entries to match your actual repository. Add any other existing modules, model files, or folders that are important to running the application.

## 🚀 Getting Started

Follow these steps to run the project locally.

### Prerequisites

Install the following:

- Python 3.10 or a compatible version for your dependencies
- MySQL Server
- Git
- A code editor such as VS Code

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd customer-churn-api
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure MySQL

Create the database in MySQL:

```sql
CREATE DATABASE customer_churn_db;
```

Configure your database connection using the environment variables described below.

Ensure the database user has the necessary permissions to access the database and create or modify tables as required.

### 5. Configure environment variables

Create a local `.env` file in the project root. Use the next section as a guide.

### 6. Start the application

```bash
uvicorn app.main:app --reload
```

Once the server starts, open:

- **API documentation:** http://127.0.0.1:8000/docs
- **Alternative API docs:** http://127.0.0.1:8000/redoc
- **Root endpoint:** http://127.0.0.1:8000/

The application also needs access to the trained model or pipeline at the path configured by your code. Make sure any required model artifact is available when running inference.

## ⚙️ Environment Configuration

Create `.env.example` with the following template:

```dotenv
DATABASE_URL=
JWT_SECRET_KEY=
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Set the actual values in your local `.env` file.

For example, a MySQL connection URL generally follows this format:

```text
mysql+pymysql://USERNAME:PASSWORD@HOST:3306/customer_churn_db
```

Use the database driver installed by your project. If your password contains special characters, URL-encode them appropriately.

Generate a strong, random JWT secret for local development. Never use the example values as real secrets.

**Security rules:**

- Never commit `.env` to GitHub.
- Keep `.env.example` free of real credentials.
- Do not publish access tokens, private customer data, or database dumps.
- If a secret is accidentally pushed, rotate it immediately; deleting the file in a later commit does not remove it from Git history.

## 📡 API Documentation

The endpoints below describe the intended application workflow. All protected endpoints require a valid bearer token.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Basic application response |
| GET | `/health` | Health check |
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Authenticate and receive a token |
| POST | `/predict-churn` | Generate a customer churn prediction |
| GET | `/predictions` | Retrieve the current user's prediction history |

### 🔑 Authentication workflow

**Step 1 — Register**

Send a JSON request to `/auth/register`:

```json
{
  "email": "user@example.com",
  "password": "ChooseA_StrongPassword123"
}
```

The application validates the request and stores a password hash rather than the original password.

**Step 2 — Login**

Send a form-encoded request to `/auth/login`.

FastAPI's `OAuth2PasswordRequestForm` expects these fields:

```text
username=user@example.com
password=ChooseA_StrongPassword123
```

The `username` field carries the email address in this implementation.

A successful login returns an access token similar in structure to:

```json
{
  "access_token": "<JWT_ACCESS_TOKEN>",
  "token_type": "bearer",
  "expires_in": 1800
}
```

The token value above is a placeholder, not a real credential.

**Step 3 — Authorize requests**

Use the token in the HTTP authorization header:

```http
Authorization: Bearer <JWT_ACCESS_TOKEN>
```

In Swagger UI, click **Authorize** and enter your login credentials through the OAuth2 form. Swagger can then send the token with protected requests.

### 🤖 Generate a churn prediction

Send a POST request to `/predict-churn` with the customer features expected by your prediction request schema.

Example feature fields may include tenure, contract type, monthly charges, total charges, internet service, and support options. The exact JSON structure and permitted values must match the schema implemented in your repository.

A successful response should contain the fields defined by your prediction response schema, such as the predicted churn class and, if implemented, churn probability.

### 📜 Retrieve prediction history

Call `GET /predictions` with a valid bearer token.

The application filters prediction records by the authenticated user's ID, so each user can retrieve their own associated prediction history.

For exact request and response examples, use the interactive `/docs` page generated from your running application.

## 🔐 Security Implementation

Security is an important part of this project.

### Password hashing

Passwords are hashed using `pwdlib` before being stored in MySQL. During login, the submitted password is verified against the stored hash.

The application does not need to decrypt stored passwords.

### JWT authentication

After successful login, the API issues a signed JWT containing the user's identifier and an expiration time.

Protected endpoints validate the token and identify the current user before performing the requested operation.

### User-specific data access

Prediction records include a user association. The history endpoint filters records using the authenticated user's ID instead of returning all prediction records.

### Request validation

Pydantic schemas validate incoming user data, helping reject malformed requests before processing.

### Environment-based secrets

Database credentials and the JWT signing secret are configured through environment variables rather than being embedded directly in source code.

> These features provide an application-level security foundation. A production deployment would also need appropriate HTTPS, rate limiting, database constraints, logging, and deployment hardening.

## 🗄️ Database Design

The application uses two principal entities.

### Users

The `users` table stores account information:

- `id`: primary key
- `email`: user email address
- `hashed_password`: stored password hash
- `created_at`: account creation timestamp

### Predictions

The `predictions` table stores prediction information:

- `id`: prediction record identifier
- `user_id`: associated user identifier
- Customer feature values used by the application
- Predicted churn class
- Churn probability, where generated

The relationship between `users.id` and `predictions.user_id` supports user-specific prediction history. The database schema should enforce the intended uniqueness and referential-integrity constraints.

## 🧪 Testing the API

You can test the API using Swagger UI or Postman.

Recommended manual test sequence:

- [ ] Register a new user.
- [ ] Attempt to register the same email again.
- [ ] Log in with valid credentials.
- [ ] Verify that an incorrect password is rejected.
- [ ] Call a protected endpoint without a token.
- [ ] Submit valid customer features to the prediction endpoint.
- [ ] Verify that the prediction is stored in MySQL.
- [ ] Retrieve prediction history with the valid token.
- [ ] Log in as a second user and verify that the first user's records are not returned.

These checks help verify the complete authentication, prediction, and database workflow. Automated tests can be added to make this validation repeatable.

## 🚧 Future Improvements

Potential enhancements include:

- [ ] Add automated tests using Pytest and FastAPI TestClient.
- [ ] Evaluate the model using precision, recall, F1-score, ROC-AUC, and a confusion matrix.
- [ ] Add database migrations and stronger schema constraints.
- [ ] Build a responsive frontend dashboard for customer information and prediction history.
- [ ] Add structured logging, rate limiting, and production-ready error handling.
- [ ] Explore model monitoring and retraining workflows.
- [ ] Deploy the application with HTTPS and secure configuration management.

These are planned enhancements, not claims about features already implemented.

## 📚 Learning Outcomes

Through this project, I explored how to:

- Integrate a trained machine learning pipeline into a Python backend.
- Design REST API endpoints using FastAPI.
- Validate requests using Pydantic.
- Connect Python applications to MySQL using SQLAlchemy.
- Implement password hashing and JWT-based authentication.
- Associate stored records with authenticated users.
- Test API workflows using Swagger UI.
- Manage configuration and secrets outside source code.

## 👩‍💻 About the Project

This project was developed as part of my learning journey in Python backend development and machine learning integration.

It helped me understand how to connect a trained ML model with REST APIs, relational databases, and authentication mechanisms to create a more complete application.

**Built with Python, machine learning, backend development, and a focus on secure data access.**

---

⭐ If you find this project useful, feel free to explore the code and share feedback.
