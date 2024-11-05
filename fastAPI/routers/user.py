from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.openapi.utils import status_code_ranges
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from models.user import User
from models.task import Task
from schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify
import logging

router = APIRouter(prefix="/user", tags=["user"])
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")


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


@router.put('/update')
async def update_user(update_user: UpdateUser, db: Annotated[Session, Depends(get_db)], user_id: int):
    """Update user"""
    user = db.query(User).get(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    db.execute(update(User).where(User.id == id).values(
        username=user.username,
        firstname=user.firstname,
        age=user.age,
        lastname=user.lastname
    ))
    db.commit()


@router.delete('/delete/{user_id}')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
  """
  Удаляет пользователя и все связанные с ним задачи.
  """
  # Удаление задач пользователя
  db.execute(delete(Task).where(Task.user_id == user_id))

  # Удаление пользователя
  db.execute(delete(User).where(User.id == user_id))

  db.commit()

  return {"message": f"User with ID {user_id} deleted successfully."}



@router.get("/{user_id}/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
  """
  Возвращает список задач конкретного пользователя по его id.
  """
  tasks = db.query(Task).filter(Task.user_id == user_id).all()

  if not tasks:
    raise HTTPException(status_code=404, detail="User not found.")

  task_data = [
    {
      "id": task.id,
      "content": task.content,
      "completed": task.completed,
      "user_id": task.user_id,
    }
    for task in tasks
  ]
  return task_data