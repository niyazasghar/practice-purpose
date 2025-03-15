import uuid
from sqlalchemy import Column, String, Date, Integer
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from app.db import Base


# Our User model extends FastAPI Users' base class for UUID-based users.
# It automatically includes fields such as email, hashed_password, is_active, etc.
# Here, we add extra fields: username, dob (date of birth), and age.
class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    username = Column(String, unique=True, index=True, nullable=False)
    dob = Column(Date, nullable=True)
    age = Column(Integer, nullable=True)
class Desktop(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "desktop"
    password = Column(String, nullable=True)
