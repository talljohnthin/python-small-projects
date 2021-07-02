from fastapi import APIRouter, status, HTTPException
from typing import List
from pydantic import BaseModel
from api.models.authusers import AuthUsers

router = APIRouter(tags=["Auth Users"])


class AuthUserResponse(BaseModel):
    id: int
    name: str


class AuthUserResponseLogin(BaseModel):
    name: str
    authenticated: bool


@router.get("/auth/", status_code=status.HTTP_200_OK, response_model=List[AuthUserResponse])
async def get_auth_users():
    authusers = await AuthUsers.objects.all()
    print(authusers)
    if len(authusers) <= 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return authusers


@router.post("/auth/login", status_code=status.HTTP_200_OK, response_model=AuthUserResponseLogin)
async def get_auth_users(username: str, password: str):
    authuser = await AuthUsers.objects.filter((AuthUsers.username == username) & (AuthUsers.password == password)).all()
    if len(authuser) <= 0:
        raise HTTPException(
            status_code=404, detail="Invalid username or password")
    user = authuser[0]
    return {
        "name": user.name,
        "authenticated": True
    }
