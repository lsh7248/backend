"""
Owner: LSH
"""
import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

app = FastAPI()


@app.get("/")
async def root():
    """
    :return: Hello World
    """
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """
    :param
    - **name** :My Name

    :return: Hello Name
    """
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
