from todo_backend.domain.todo.entities import Todo


class TodoResponse:
    def __init__(self, todo_id: str, text: str, done: bool):
        self.id = todo_id
        self.text = text
        self.done = done

    @staticmethod
    def from_todo(todo: Todo):
        return TodoResponse(todo_id=todo.id, text=todo.text, done=todo.done)