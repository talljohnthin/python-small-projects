from typing import List
import databases
import sqlalchemy
import ormar

DATABASE_URL = "postgresql://postgres:realtrue@localhost:5432/local_db"

metadata = sqlalchemy.MetaData()
database = databases.Database(DATABASE_URL)


# class Users(ormar.Model):
#     class Meta:
#         tablename = "users"
#         metadata = metadata
#         database = database

#     id: int = ormar.Integer(primary_key=True)
#     name: str = ormar.String(max_length=255)
