
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.user_model import User
from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from app.schemas.user import UserCreate, UserResponse


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# User Registration

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    # Check whether the email is already registered
    existing_user = (
        db.query(User)
        .filter(User.email == str(user_data.email))
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists"
        )

    # Hash the password before saving it
    new_user = User(
        email=str(user_data.email),
        hashed_password=hash_password(user_data.password)
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to create account"
        )

    return new_user

# User Login

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # The OAuth2 username field contains the user's email
    user = (
        db.query(User)
        .filter(User.email == form_data.username)
        .first()
    )

    # Verify credentials without revealing which one is wrong
    if not user or not verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # Generate an expiring JWT access token
    access_token = create_access_token(user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }
