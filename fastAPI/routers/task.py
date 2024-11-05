from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.openapi.utils import status_code_ranges
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from models.task import Task
from models.user import User
from schemas import CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify
import logging

router = APIRouter(prefix="/task", tags=["task"])
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    """Возвращает список всех пользователей."""
    try:
        tasks = db.query(Task).all()
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
    except Exception as ex:
        logging.error(ex)

@router.get('/{task_id}')
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    """Возвращает пользователя по ID."""
    task = db.query(Task).get(task_id)
    if task:
        ans = {
            "id": task.id,
            "content": task.content,
            "completed": task.completed,
            "user_id": task.user_id,
        }
        return ans
    else:
        return {"message": "Task not found"}, status.HTTP_404_NOT_FOUND


@router.post('/create')
async def create_task(task: CreateTask, db: Annotated[Session, Depends(get_db)]):
    """Создает нового пользователя."""

    # Проверка наличия пользователя
    user_exists = db.query(User).filter(User.id == task.user_id).first() is not None

    if user_exists:
        # Пользователь с заданным ID найден
        db.execute(insert(Task).values(
            title=task.title,
            content=task.content,
            priority=task.priority,
            completed=task.completed,
            user_id=task.user_id,
        ))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED,
                'transaction': 'Successful'}
    else:
        # Пользователя с заданным ID не существует
        return {'status_code': status.HTTP_400_BAD_REQUEST,
                'transaction': 'User not found'}


@router.put('/update')
async def update_task(update_task: UpdateTask, db: Annotated[Session, Depends(get_db)], task_id: int):
    """Update user"""
    task = db.query(Task).get(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    db.execute(update(Task).where(Task.id == task_id).values(
        content=task.content,
        completed=task.completed,
        user_id=task.user_id,
        lastname=task.lastname
    ))
    db.commit()

@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], task_id : int):
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
