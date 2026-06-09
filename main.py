from fastapi import FastAPI
from src.utils.db import Base,engine
from src.tasks.model import TaskModel
from src.tasks.router import task

Base.metadata.create_all(engine)



app = FastAPI(title="This is first page")
app.include_router(task)

@app.get("/")
def home():
    return {"status" : "This is homepage"}
