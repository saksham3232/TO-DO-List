from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define ToDo item structure
class ToDoItem(BaseModel):
    id: int
    title: str
    description: str

# In-memory "database"
todo_list = {}

# Create a new ToDo
@app.post("/todos/", response_model=ToDoItem)
def create_todo_item(todo_item: ToDoItem):
    if todo_item.id in todo_list:
        raise HTTPException(status_code=400, detail="To-Do item already exists")
    todo_list[todo_item.id] = todo_item
    return todo_item

# Read a ToDo by ID
@app.get("/todos/{todo_id}", response_model=ToDoItem)
def read_todo_item(todo_id: int):
    if todo_id not in todo_list:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    return todo_list[todo_id]

# Read all ToDos
@app.get("/todos/", response_model=list[ToDoItem])
def read_all_todo_items():
    return list(todo_list.values())

# Update a ToDo
@app.put("/todos/{todo_id}", response_model=ToDoItem)
def update_todo_item(todo_id: int, todo_item: ToDoItem):
    if todo_id not in todo_list:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    todo_list[todo_id] = todo_item
    return todo_item

# Delete a ToDo
@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int):
    if todo_id not in todo_list:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    del todo_list[todo_id]
    return {"detail": "To-Do item deleted successfully"}