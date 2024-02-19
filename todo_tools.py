import pickle
from pydantic import BaseModel
from typing import List
import os

class Todo(BaseModel):
    id: str
    text: str
    type: str
    done: bool

class TodoList(BaseModel):
    user: str
    todos: List[Todo]

class TodoAppUser(BaseModel):
    user: str
    personal_todos: List[Todo]
    work_todos: List[Todo]

def load_todos(filename: str, user_name: str):
    try:
        with open(filename, 'rb') as f:
            model = pickle.load(f)

        for users in model:
            if users.user == user_name:
                return users.todos

        return []

    except:
        print("smth wrong")
        return []

def save_todos(filename: str, user_name: str, todo_list: [Todo]):
    try:
        with open(filename, 'r+b') as f:
            f.seek(0, os.SEEK_END)
            if f.tell():
                f.seek(0)
                model = pickle.load(f)
                new_user = True
                for i, user in enumerate(model):
                    if user.user == user_name:
                        model[i] = TodoList(user=user_name, todos=todo_list)
                        new_user=False
                if new_user:
                    model.append(TodoList(user=user_name, todos=todo_list))

                f.seek(0)
                pickle.dump(model, f)
            else:
                f.seek(0)
                model=[]
                model.append(TodoList(user=user_name, todos=todo_list))
                pickle.dump(model, f)
    except FileNotFoundError:
        with open(filename, 'w+b') as f:
            model = []
            model.append(TodoList(user=user_name, todos=todo_list))
            pickle.dump(model, f)

'''


def update_todo(todo_list, new_todo: Todo):
    for i, todo in enumerate(todo_list):
        print(todo)
        if todo.id == new_todo.id:
            todo_list[i] = Todo(id=new_todo.id, text=new_todo.text, state=new_todo.state)
    return todo_list

def delete_todo(todo_list, id):
    return [todo for todo in todo_list if todo.id != id]
    
'''

