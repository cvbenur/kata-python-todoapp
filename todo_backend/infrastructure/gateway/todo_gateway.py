import logging

from todo_backend.domain.todo.gateway import TodoGatewayInterface
from todo_backend.domain.todo.entities import Todo
from todo_backend.infrastructure.repository.todo_repository import TodoRepository

class TodoGateway(TodoGatewayInterface):
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository
        self.logger = logging.getLogger("TodoGateway")

    def get_all_todos(self) -> list[Todo]:
        ret = self.todo_repository.get_all()
        return list(map(lambda x: x.to_todo(), ret))

    def get_todo_by_id(self, todo_id: str) -> Todo | None:
        ret = self.todo_repository.get_one_by_id(todo_id)
        return ret.to_todo() if ret else None

    def create_todo(self, text: str) -> Todo:
        ret = self.todo_repository.create(text=text)
        return ret.to_todo()

    def update_todo_by_id(self, todo_id: str, text: str | None, done: bool | None) -> Todo | None:
        to_update = self.todo_repository.get_one_by_id(todo_id)
        if to_update is None:
            return None
        if text is not None:
            to_update.text = text
        if done is not None:
            to_update.done = done
        ret = self.todo_repository.update(to_update.id, to_update.text, to_update.done)
        return ret.to_todo() if ret else None

    def delete_todo_by_id(self, todo_id: str) -> Todo | None:
        ret = self.todo_repository.delete_one_by_id(todo_id)
        return ret.to_todo() if ret else None