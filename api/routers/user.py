from fastapi import APIRouter
from typing import List
from api.models.user import Users

router = APIRouter()


@router.get("/users/", tags=["users"], response_model=List[Users])
async def get_users():
    users = await Users.objects.all()
    return users


@router.post("/users/", tags=["users"], response_model=Users)
async def create_user(user: Users):
    await user.save()
    return user
