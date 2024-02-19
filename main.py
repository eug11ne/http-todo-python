from  fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from todo_tools import *
from typing import List

app = FastAPI()

origins = [
    "http://localhost:1234",
    "http://localhost:8000",
    "https://65d2fce7e2099c0008c0e5d1--charming-nasturtium-b95241.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/download/{who}")
def ret_todo_list(who: str):
    todos=load_todos('todoapp.json', who)
    return todos

@app.post("/upload/{who}")
def save_todo_list(who, todo: List[Todo]):
    save_todos('todoapp.json', who, todo)
    return True

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)







''' ff = [Todo(id='101', text='PERSddddddrrrddd TOFO', type='Personal', done=True),
          Todo(id='1012', text='PERSddddddrrrdd  dTOFO', type='Personal', done=True),
          Todo(id='10134', text='PERSddddddrrrdd dTOFO', type='Personal', done=True),
          Todo(id='10145', text='PERSddddddrrrdd211dTOFO', type='Personal', done=True),
          Todo(id='10156', text='PERSddddddrr222rdddTOFO', type='Work', done=False),
          Todo(id='101516', text='PERSddddddrr222rdddTOFO', type='Work', done=False),
          Todo(id='101526', text='PERSddddddrr222rdddTOFO', type='Work', done=False),
          Todo(id='101546', text='PERSddddddrr222rdddTOFO', type='Work', done=False)]
    save_todos('todoapp.json', 'sam', ff)
    
'''