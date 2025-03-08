from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.db import create_db_and_tables
from app.schemas import UserRead, UserCreate, UserUpdate
from app.users import fastapi_users, auth_backend, current_active_user

# Lifespan context manager: used here to initialize the database tables at startup.
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# Include authentication and user management routers from FastAPI Users.
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

# Example of a protected route which requires an active user.
@app.get("/authenticated-route")
async def authenticated_route(user=Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
