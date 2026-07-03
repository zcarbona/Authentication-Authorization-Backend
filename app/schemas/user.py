from pydantic import BaseModel, EmailStr, ConfigDict

class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True) 


class ResetPasswordRequest(BaseModel):
    old_password: str
    new_password: str
    