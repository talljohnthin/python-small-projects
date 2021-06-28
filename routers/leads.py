from fastapi import APIRouter

router = APIRouter()

@router.get("/leads/", tags=["leads"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]