from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users():
  return JSONResponse(users)

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
  next_id = str(max(int(key) for key in users.keys()) + 1)
  users[next_id] = f"Имя: {username}, возраст: {age}"
  return f"User {next_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
  if user_id not in users:
    raise HTTPException(status_code=404, detail="User not found")
  users[user_id] = f"Имя: {username}, возраст: {age}"
  return f"The user {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
  if user_id not in users:
    raise HTTPException(status_code=404, detail="User not found")
  del users[user_id]
  return f"User {user_id} has been deleted"

# Запускаем приложение
if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)

