from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.model import TaskModel
from fastapi import HTTPException

def create_task(body:TaskSchema,db : Session):
    data = body.model_dump()
    new_task = TaskModel(title = data["title"],description = data["description"],is_completed = data["is_completed"])

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status" : "task create Sucessfully"}

def get_all_task(db : Session):
    task = db.query(TaskModel).all() # run a query on database of table whose table schema is TaskModel and extract all data
    return {"data" : task}

def get_one_task(id : int , db:Session):
    one_task = db.query(TaskModel).get(id) # run a query on database and fetch a data of give id

    if not one_task:
        raise HTTPException(status_code=404,detail="Task not found.")
    
    return {"status":"Task fetch successfully","Data" : one_task}
