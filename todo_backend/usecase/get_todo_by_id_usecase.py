from todo_backend.domain.todo.gateway import TodoGatewayInterface
from todo_backend.domain.todo.entities import Todo


class GetTodoByIdUseCase:
    def __init__(self, todo_gateway: TodoGatewayInterface):
        self.todo_gateway = todo_gateway

    def execute(self, todo_id: str) -> Todo | None:
        return self.todo_gateway.get_todo_by_id(todo_id)