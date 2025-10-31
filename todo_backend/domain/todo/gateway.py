from abc import ABC, abstractmethod
from todo_backend.domain.todo.entities import Todo

class TodoGatewayInterface(ABC):

    @abstractmethod
    def get_all_todos(self) -> list[Todo]:
        pass

    @abstractmethod
    def get_todo_by_id(self, todo_id: str) -> Todo | None:
        pass

    @abstractmethod
    def create_todo(self, text: str) -> Todo:
        pass

    @abstractmethod
    def update_todo_by_id(self, todo_id: str, text: str | None, done: bool | None):
        pass

    @abstractmethod
    def delete_todo_by_id(self, todo_id: str) -> Todo | None:
        pass