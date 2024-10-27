from sqlalchemy import Column, Integer, String

from backend.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)


    tasks = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        from .task import Task
        self.tasks = relationship("Task", back_populates="user")

