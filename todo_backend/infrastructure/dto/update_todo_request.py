from pydantic import BaseModel, Field


class UpdateTodoRequest(BaseModel):
    text: str | None = Field(default=None)
    done: bool | None = Field(default=None)