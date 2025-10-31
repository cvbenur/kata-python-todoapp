from pydantic import BaseModel


class CreateTodoRequest(BaseModel):
    text: str