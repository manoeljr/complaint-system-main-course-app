from fastapi import FastAPI

from db import database
from resources.routes import api_router


app = FastAPI(
    title="C.S.M.C.A",
    description="API REST - Complaint System Main Course App",
    version="1.0",
    openapi_url="/docs/json",
)
app.include_router(api_router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
