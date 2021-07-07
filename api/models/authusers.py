import ormar
from datetime import datetime
from api.database import metadata, database


class AuthUsers(ormar.Model):
    class Meta:
        tablename = "authusers"
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=255)
    username: str = ormar.String(max_length=255)
    password: str = ormar.String(max_length=255)
    createdAt: datetime = ormar.DateTime(default=datetime.now())
    updatedAt: datetime = ormar.DateTime(default=datetime.now())
