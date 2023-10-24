from fastapi import FastAPI
from . import models
from .database import engine
from .routers import student

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(student.app)

@app.get('/')
def test_route():
    return {"message": "This is test route"}