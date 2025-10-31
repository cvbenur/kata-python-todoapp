from todo_backend.domain.todo.gateway import TodoGatewayInterface

class DeleteTodoByIdUseCase:
    def __init__(self, todo_gateway: TodoGatewayInterface):
        self.todo_gateway = todo_gateway

    def execute(self, todo_id: str):
        ret = self.todo_gateway.delete_todo_by_id(todo_id)
        return ret