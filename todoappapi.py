from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class ToDo(BaseModel):
    task: str
    status: str

class UpdateTodo(BaseModel):
    task: Optional[str] = None
    status: Optional[str] = None

todos = {
    1: ToDo(
        task = "Study",
        status = "NOT DONE"
    ),
    2: ToDo(
        task = "Assignment",
        status = "NOT DONE"
    ),
}



@app.get("/")
def index():
    return {
        "Welcome to todoapp!!"
        "Insert these characters to the url link to continue:"
        "/get-task/{id}"
        "/get-task-by-task/{todo_id}"
        "/create-task/{todo_id}"
        "/update-task/{todo_id}"
        "/delete-task/{todo_id}"
        }



@app.get("/get-task/{id}")
def get_todo(id: int = Path(description = "The ID of task is not available")):
    return todos[id]



@app.get("/get-todo-by-task/{todo_id}")
def get_todo(task: str):
    for todo_id in todos:
        if todos[todo_id].task == task:
            return todos[todo_id]
    return {"Task DOES NOT exist"}



#POST method
@app.post("/create-task/{todo_id}")
def add_todo(todo_id: int, todo: ToDo):
    if todo_id in todos:
        return {"Task DOES NOT exist"}
    todos[todo_id] = todo
    return todos[todo_id]



# PUT method
@app.put("/update-task/{todo_id}")
def update_todo(todo_id: int, todo: UpdateTodo):
    if todo_id not in todos:
        return {"Task DOES NOT exist"}
    if todo.task != None:
        todos[todo_id].task = todo.task
    if todo.status != None:
        todos[todo_id].status = todo.status
    return todos[todo_id]



#DELETE method
@app.delete("/delete-task/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        return{"Task DOES NOT exist"}
    del todos[todo_id]
    return {"Task has been deleted successful"}