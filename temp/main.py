from fastapi import FastAPI

from .task import task_router
from .user import user_router

app = FastAPI()

@app.get('/')
async def root():
  return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)
