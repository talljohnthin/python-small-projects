import databases
import sqlalchemy

DATABASE_URL = "postgresql://postgres:realtrue@localhost:5432/local_db"

metadata = sqlalchemy.MetaData()
database = databases.Database(DATABASE_URL)
