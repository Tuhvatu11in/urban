from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <h1>Главная страница</h1>
    """

@app.get("/user/admin", response_class=HTMLResponse)
async def admin():
    return """
    <h1>Вы вошли как администратор</h1>
    """

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def user_by_id(user_id: int):
    return f"""
    <h1>Вы вошли как пользователь № {user_id}</h1>
    """

@app.get("/user", response_class=HTMLResponse)
async def user_info(request: Request):
    query_params = request.query_params
    username = query_params.get("username")
    age = query_params.get("age")
    if username and age:
        return f"""
        <h1>Информация о пользователе.</h1>
        <p>Имя: {username}</p>
        <p>Возраст: {age}</p>
        """
    else:
        return "Некорректные данные"

