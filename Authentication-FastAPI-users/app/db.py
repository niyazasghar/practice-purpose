from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from app.models import User  # Our SQLAlchemy user model

# Use an async SQLite database (for development; swap for production)
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Create the async engine and session maker
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Create all tables (not recommended for production; use a migration tool like Alembic)
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency to provide an async DB session
async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session

# Dependency to get the FastAPI Users database adapter
async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
