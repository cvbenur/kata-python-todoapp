from todo_backend.infrastructure.config.db import Base, engine
from sqlalchemy import Column, String, Boolean, Integer

from todo_backend.domain.todo.entities import Todo


class TodoDao(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    done = Column(Boolean, default=False)

    def to_todo(self) -> Todo:
        return Todo(todo_id=str(self.id), text=self.text, done=self.done)

Base.metadata.create_all(engine)