from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users = []

class User(BaseModel):
 id: int
 username: str
 age: int

@app.get("/")
async def get_users(request: Request):
 return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
 next_id = 1 if len(users) == 0 else users[-1].id + 1
 new_user = User(id=next_id, username=username, age=age)
 users.append(new_user)
 return JSONResponse(new_user, status_code=201)

@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: int):
 user = next((u for u in users if u.id == user_id), None)
 if user:
  return templates.TemplateResponse("users.html", {"request": request, "user": user})
 else:
  raise HTTPException(status_code=404, detail="User was not found")

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
 user = next((u for u in users if u.id == user_id), None)
 if user:
  user.username = username
  user.age = age
  return JSONResponse(user)
 else:
  raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
 user = next((u for u in users if u.id == user_id), None)
 if user:
  users.remove(user)
  return JSONResponse(user)
 else:
  raise HTTPException(status_code=404, detail="User was not found")

# Создание пользователей
create_user(username="UrbanUser", age=24)
create_user(username="UrbanTest", age=22)
create_user(username="Capybara", age=60)

# Запускаем приложение
if __name__ == "__main__":
 import uvicorn
 uvicorn.run(app, host="0.0.0.0", port=8000)
