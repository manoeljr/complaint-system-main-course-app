import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API online !"}


@app.get("/ping/")
async def pong():
    return {"message": "pong"}


if __name__ == '__main__':
    uvicorn.run(app)

