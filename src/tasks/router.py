from fastapi import APIRouter , Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from  src.utils.db import get_db


task = APIRouter(prefix="/tasks")


@task.post("/create")
def task_create(body : TaskSchema,db = Depends(get_db)): # dependency injection
    return controller.create_task(body,db)

@task.get("/get_all")
def get_task(db = Depends(get_db)):
    return controller.get_all_task(db)

@task.get("/get_one_task/{id}")
def get_one_data(id : int , db = Depends(get_db)):
    return controller.get_one_task(id,db)
