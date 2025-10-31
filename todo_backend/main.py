import uvicorn
import logging

from fastapi import FastAPI
from todo_backend.infrastructure.routers import todos

app = FastAPI()
app.include_router(todos.router)

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)