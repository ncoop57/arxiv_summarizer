import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel


class Message(BaseModel):
    code: str


app = FastAPI()


@app.post("/")
async def root(msg: Message):
    return msg


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
