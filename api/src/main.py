import uvicorn
from fastapi import FastAPI
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from .models import columns as ColumnsModel
from src import schemas
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url="postgresql://postgres:postgres@db:5432")

@app.post("/column/", response_model=schemas.Columns)
def create_user(column: schemas.Columns):
    db_user = ColumnsModel(
        title=column.title, position=column.position
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)