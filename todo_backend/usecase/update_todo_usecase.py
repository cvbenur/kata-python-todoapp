from todo_backend.domain.todo.entities import Todo
from todo_backend.domain.todo.gateway import TodoGatewayInterface


class UpdateTodoUseCase:
    def __init__(self, todo_gateway: TodoGatewayInterface):
        self.todo_gateway = todo_gateway

    def execute(self, todo_id: str, text: str | None, done: bool | None) -> Todo | None:
        ret = self.todo_gateway.update_todo_by_id(todo_id, text, done)
        return ret