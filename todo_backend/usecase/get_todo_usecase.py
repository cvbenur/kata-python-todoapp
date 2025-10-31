from todo_backend.infrastructure.gateway.todo_gateway import TodoGateway
from todo_backend.domain.todo.entities import Todo


class GetAllTodosUseCase:
    def __init__(self, todo_gateway: TodoGateway):
        self.todo_gateway = todo_gateway

    def execute(self) -> list[Todo]:
        return self.todo_gateway.get_all_todos()