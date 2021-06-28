from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI

import ormar

DATABASE_URL = "postgresql://postgres:realtrue@localhost:5432/local_db"

app = FastAPI()
metadata = sqlalchemy.MetaData()
database = databases.Database(DATABASE_URL)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


class User(ormar.Model):
    class Meta:
        tablename = "users"
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=255)

@app.get("/users/", response_model=List[User])
async def get_users():
    users = await User.objects.all()
    return users

@app.post("/user/", response_model=User)
async def create_user(user: User):
    await user.save()
    return user