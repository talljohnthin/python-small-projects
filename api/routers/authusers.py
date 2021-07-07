from fastapi import APIRouter, status, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from api.auth import AuthHandler
from api.models.authusers import AuthUsers

router = APIRouter(tags=["Auth Users"])

auth_handler = AuthHandler()


class AuthUserResponse(BaseModel):
    id: int
    name: str


class AuthUserResponseLogin(BaseModel):
    name: str
    authenticated: bool
    token: str


class AuthUserResponseRegister(BaseModel):
    name: str


class AuthenticatedResponse(BaseModel):
    name: str


@router.get("/auth/", status_code=status.HTTP_200_OK, response_model=List[AuthUserResponse])
async def get_auth_users():
    authusers = await AuthUsers.objects.all()
    if len(authusers) <= 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return authusers


@router.post("/auth/login", status_code=status.HTTP_200_OK, response_model=AuthUserResponseLogin)
async def get_auth_users(username: str, password: str):
    authuser = await AuthUsers.objects.filter(AuthUsers.username == username).all()

    if len(authuser) <= 0:
        raise HTTPException(
            status_code=404, detail="Invalid username")

    user = authuser[0]

    if not auth_handler.verify_password(password, user.password):
        raise HTTPException(
            status_code=404, detail="Invalid password")
    else:
        token = auth_handler.encode_token(user.username)
        return {
            "name": user.name,
            "authenticated": True,
            "token": token
        }


@router.post("/auth/register", status_code=status.HTTP_200_OK, response_model=AuthUserResponseRegister)
async def create_users(name: str, username: str, password: str):
    authuser = await AuthUsers.objects.filter(AuthUsers.username == username).all()
    if len(authuser) > 0:
        raise HTTPException(status_code=400, detail="Username already exist")

    hash_password = auth_handler.get_password_hash(password)
    new_user = await AuthUsers.objects.create(name=name, username=username, password=hash_password)
    new_user.save()
    return {"name": name}


@router.get('/protected',  status_code=status.HTTP_200_OK, response_model=AuthenticatedResponse)
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {'name': username}
