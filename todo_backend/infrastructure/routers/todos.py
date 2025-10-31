import logging

from todo_backend.infrastructure.config.db import get_db_session
from todo_backend.infrastructure.dto.create_todo_request import CreateTodoRequest
from todo_backend.infrastructure.dto.update_todo_request import UpdateTodoRequest
from todo_backend.infrastructure.gateway.todo_gateway import TodoGateway
from todo_backend.infrastructure.dto.todo_response import TodoResponse
from fastapi import APIRouter, HTTPException

from todo_backend.infrastructure.repository.todo_repository import TodoRepository
from todo_backend.usecase.create_todo_usecase import CreateTodoUseCase
from todo_backend.usecase.delete_todo_by_id_usecase import DeleteTodoByIdUseCase
from todo_backend.usecase.get_todo_by_id_usecase import GetTodoByIdUseCase
from todo_backend.usecase.get_todo_usecase import GetAllTodosUseCase
from todo_backend.usecase.update_todo_usecase import UpdateTodoUseCase

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)

todos_repository = TodoRepository(db_session=next(get_db_session()))
todos_gateway = TodoGateway(todos_repository)
get_all_todos_use_case = GetAllTodosUseCase(todos_gateway)
get_todo_by_id_use_case = GetTodoByIdUseCase(todos_gateway)
create_todo_use_case = CreateTodoUseCase(todos_gateway)
update_todo_use_case = UpdateTodoUseCase(todos_gateway)
delete_todo_by_id_use_case = DeleteTodoByIdUseCase(todos_gateway)

logger = logging.getLogger("TodoRouter")

@router.get("/")
async def get_todos():
    all_todos = get_all_todos_use_case.execute()
    logger.info("Found {} todos".format(len(all_todos)))
    return list(map(lambda todo: TodoResponse(todo_id=todo.id, text=todo.text, done=todo.done), all_todos))

@router.get("/{todo_id}")
async def get_todos_id(todo_id: str):
    ret = get_todo_by_id_use_case.execute(todo_id)
    if ret is None:
        logger.info("No todo found for id {}".format(todo_id))
        raise HTTPException(status_code=404, detail="No item found for id: {}".format(todo_id))
    logger.info("Found todo : {}".format(ret.__dict__))
    return TodoResponse.from_todo(ret)

@router.post("/", status_code=201)
async def create_todos(body: CreateTodoRequest):
    if body.text is None or body.text == "":
        logger.info("Missing 'text' parameter in request")
        raise HTTPException(status_code=400, detail="Parameter 'text' must be present and non empty")
    logger.info("Creating new todo : {}".format(body.text))
    ret = create_todo_use_case.execute(body.text)
    logger.info("New todo created : {}".format(ret.__dict__))
    return TodoResponse.from_todo(ret)

@router.put("/{todo_id}")
@router.patch("/{todo_id}")
async def update_todo(todo_id: str, body: UpdateTodoRequest):
    if (body.text is None or body.text == "") and (body.done is None):
        logger.info("Missing parameters in request")
        raise HTTPException(status_code=400, detail="At least one of 'text' and 'done' must be present and non empty")
    logger.info("Updating todo with id : {}".format(todo_id))
    ret = update_todo_use_case.execute(todo_id, body.text, body.done)
    if ret is None:
        logger.info("No todo found for id : {}".format(todo_id))
        raise HTTPException(status_code=404, detail="No item found for id: {}".format(todo_id))
    logger.info("Updated todo : {}".format(ret.__dict__))
    return TodoResponse.from_todo(ret)

@router.delete("/{todo_id}", status_code=204)
async def delete_todos_id(todo_id: str):
    logger.info("Deleting todo with id : {}".format(todo_id))
    ret = delete_todo_by_id_use_case.execute(todo_id)
    if ret is None:
        logger.info("No todo found for id : {}".format(todo_id))
        raise HTTPException(status_code=404, detail="No item found for id: {}".format(todo_id))
    logger.info("Deleted todo : {}".format(ret.__dict__))
    return TodoResponse.from_todo(ret)