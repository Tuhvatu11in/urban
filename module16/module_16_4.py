from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
  id: int
  username: str
  age: int

@app.get("/users")
async def get_users():
  return JSONResponse(users)

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
  next_id = 1 if len(users) == 0 else users[-1].id + 1
  new_user = User(id=next_id, username=username, age=age)
  users.append(new_user)
  return JSONResponse(new_user, status_code=201)

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

# Запускаем приложение
if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)
