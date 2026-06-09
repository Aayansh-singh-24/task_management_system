from fastapi import APIRouter , Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from  src.utils.db import get_db


task = APIRouter(prefix="/tasks")


@task.post("/create")
def task_create(body : TaskSchema,db = Depends(get_db)): # dependency injection
    return controller.create_task(body,db)
