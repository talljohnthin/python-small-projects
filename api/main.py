
from fastapi import FastAPI
from .routers import lead, authusers
from api.database import database

app = FastAPI(
    title="Insurance API Admin",
    description="This api is use for the admin of the insurance.",
    version="1.0"
)

# initialize db connection
app.state.database = database

app.include_router(authusers.router)
app.include_router(lead.router)


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
