from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.core.database import get_db
from app.models.user import User
from app.schemas.auth import LoginRequest, Token
from app.schemas.user import CreateUserRequest, UserResponse,ResetPasswordRequest
from app.core.security import hash_password,verify_password,create_access_token
from app.api.dependencies import get_current_user
router = APIRouter(tags=["Authentication"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: CreateUserRequest,
    db: Session = Depends(get_db),
):
    existing_user = (
        db.query(User)
        .filter(
            or_(
                User.username == user.username,
                User.email == user.email,
            )
        )
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exists.",
        )
    # Hash password
    hashed_password = hash_password(user.password)

    # Create User object
    user_db = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_admin=False,
        is_verified=False,
        is_active=True,

    )
    
    # Save to database
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    # Return created user
    return user_db


@router.post(
    "/login",
    response_model=Token,
    status_code=status.HTTP_200_OK
)

def login(credentials: LoginRequest,db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == credentials.username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    if not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        ) 
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is disabled"
        )
    access_token = create_access_token(
        data={
            "sub":user.username
        }
    )
    return Token(
    access_token=access_token,
    token_type="bearer",
)


@router.put("/reset-password",status_code=status.HTTP_200_OK)
def reset_password(data: ResetPasswordRequest, db:Session=Depends(get_db), current_user: User=Depends(get_current_user)): #not forget this is reset so we ask for old password
    if not verify_password(data.old_password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect old password"
        ) 
    
    current_user.hashed_password = hash_password(data.new_password)
    db.commit()
    db.refresh(current_user)
    




@router.get("/me", response_model=UserResponse)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user