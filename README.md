# Todo app Back-end (Python)

This is a Todo list back-end application made with Python, using hexagonal architecture principles.
It uses a local DB (using SQLite) and comes with a test suite.

Be sure to take a look to [what's missing from this project](#whats-missing) !

## Requirements

In order for this project to run, you should have Python (at least `3.13`) installed on your machine.

## Installation & Setup

### Installation

To install, open a terminal in the root directory and run the following:
```shell
pip install -r requirements.txt
```

### Project setup

Before you can run the server, you need to:

1. Create an empty file at the root of the project, called `todos.db`.
2. Create a file at the root of the project, called `.env`, containing:
<br/>`DB_URL=sqlite:///../../todos.db`

Once all this is done, you should be good to go.

## Running the project

### Running the local server

You can run the local server using the following command:
```shell
python -m uvicorn todo_backend.main:app
```

## What's missing

Due to time constraints, several things are missing and/or could be improved.

#### Phase 1 - Critical
1. **Unit tests.** There are next to no unit tests in this project, which means there are no automatable means of checking the app for mistakes, it must be done by hand.
2. **DB session concurrency.** Currently, the entire app uses only DB session which is instantiated on startup. This can be fixed by injecting a session on each request (FastAPI's `Depends`).

#### Phase 2 - Important
1. **Request body validation.** This app possesses no custom body validation and relies on the default configuration from `pydantic`. This could be fixed by adding custom field validators in the base model classes.
2. **Underdeveloped `UseCase` classes.** The UseCase classes currently only delegate method calls. Some of the validation should be moved down from the router to the UseCase classes.
3. **Robust error handling,** through business logic exceptions.
4. **Documentation.** This can be fixed by adding docstring.

#### Phase 3 - Improvements
1. **Logging improvements.** Some simple formatting could be added in order to improve logs readability.
2. **Model enrichment.** Saving and using timestamps, todo modification history, etc.
3. **File and class naming,** following Python conventions a bit closer.
