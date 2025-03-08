import uuid
from typing import Optional
from datetime import date
from fastapi_users import models

# Schema for reading user data (excludes sensitive fields like password)
class UserRead(models.BaseUser[uuid.UUID]):
    username: str
    dob: Optional[date]
    age: Optional[int]

# Schema for creating a user (includes the password and our custom fields)
class UserCreate(models.BaseUserCreate):
    username: str
    dob: Optional[date] = None
    age: Optional[int] = None

# Schema for updating a user (all fields optional)
class UserUpdate(models.BaseUserUpdate):
    username: Optional[str]
    dob: Optional[date]
    age: Optional[int]
