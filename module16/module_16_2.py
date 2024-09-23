from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, validator, Field
from typing import Annotated

app = FastAPI()

class UserID(BaseModel):
    user_id: Annotated[int, Field(
        ...,
        gt=0,
        le=100,
        description='Enter User ID',
        example='1'
    )]

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def user_by_id(user_id: int):  # Now accepting an int directly
    return f"""
    <h1>Вы вошли как пользователь № {user_id}</h1>
    """

class UserInfo(BaseModel):
    username: Annotated[str, Field(
        ...,
        min_length=5,
        max_length=20,
        description='Enter username',
        example='UrbanUser'
    )]
    age: Annotated[int, Field(
        ...,
        ge=18,
        le=120,
        description='Enter age',
        example='24'
    )]

@app.get("/user/{username}/{age}", response_class=HTMLResponse)
async def user_info(username: str, age: int, user_info: UserInfo):
    return f"""
    <h1>Информация о пользователе.</h1>
    <p>Имя: {username}</p>
    <p>Возраст: {age}</p>
    """

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
