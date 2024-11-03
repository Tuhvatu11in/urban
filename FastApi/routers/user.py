from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.openapi.utils import status_code_ranges
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from models.user import User
from schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify
import logging

router = APIRouter(prefix="/user", tags=["user"])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    """Возвращает список всех пользователей."""
    users = db.query(User).all()
    user_data = [
        {
            "id": user.id,
            "username": user.username,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "age": user.age
        }
        for user in users
    ]
    return user_data


@router.get('/{user_id}')
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    """Возвращает пользователя по ID."""
    user = db.query(User).get(user_id)
    if user:
        ans = {
            "id": user.id,
            "username": user.username,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "age": user.age
        }
        logging.log(20, ans)
        return ans
    else:
        return {"message": "User not found"}, status.HTTP_404_NOT_FOUND


@router.post('/create')
async def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    """Создает нового пользователя."""
    db.execute(insert(User).values(username=user.username,
                                   firstname=user.firstname,
                                   age=user.age,
                                   lastname=user.lastname))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}



