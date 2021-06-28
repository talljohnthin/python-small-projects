
from fastapi import FastAPI
from .routers import user
from api.database import database

app = FastAPI()

# initialize db connection
app.state.database = database

app.include_router(user.router)


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
