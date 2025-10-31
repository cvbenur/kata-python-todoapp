from todo_backend.domain.todo.gateway import TodoGatewayInterface


class CreateTodoUseCase:
    def __init__(self, todo_gateway: TodoGatewayInterface):
        self.todo_gateway = todo_gateway

    def execute(self, text: str):
        return self.todo_gateway.create_todo(text)