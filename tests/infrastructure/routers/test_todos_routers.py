import unittest.mock as mock
import todo_backend.infrastructure.routers.todos as todos_routers

from fastapi.testclient import TestClient
from todo_backend.main import app

client = TestClient(app)


def test_get_todos():
    with mock.patch.object(todos_routers.get_all_todos_use_case, 'execute', return_value=list()):
        response = client.get("/todos")
        assert response.status_code == 200
        assert response.json() == []

def test_get_todos_id__when_item_exists__should_return_item():
    with mock.patch.object(
            todos_routers.get_todo_by_id_use_case,
            'execute',
            return_value={"id": "1", "text": "some todo", "done": False}
    ):
        response = client.get("/todos/1")
        assert response.status_code == 200
        assert response.json() == { "id": "1", "text": "some todo", "done": False }

def test_get_todos_id__when_item_doesnt_exist__should_404():
    with mock.patch.object(
            todos_routers.get_todo_by_id_use_case,
            'execute',
            return_value=None
    ):
        response = client.get("/todos/1")
        assert response.status_code == 404
        assert response.json() == {"detail": "No item found for id: 1"}

def test_create_todos__should_create_todo():
    with mock.patch.object(
            todos_routers.create_todo_use_case,
            'execute',
            return_value={"id": "2", "text": "some other todo", "done": False}
    ):
        response = client.post(
            "/todos",
            json={"text": "some other todo"}
        )
        assert response.status_code == 201
        assert response.json() == {"id": "2", "text": "some other todo", "done": False}

def test_create_todos__with_missing_text_parameter__should_422():
    response = client.post(
        "/todos",
        json={}
    )
    assert response.status_code == 422

def test_create_todos__with_empty_text_parameter__should_400():
    response = client.post(
        "/todos",
        json={"text": ""}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Parameter 'text' must be present and non empty"}

def test_update_todos_id__should_update_todo():
    with mock.patch.object(
            todos_routers.update_todo_use_case,
            'execute',
            return_value={"id": "1", "text": "updated todo", "done": False}
    ):
        put_response = client.put(
            "/todos/1",
            json={"text": "updated todo"}
        )
        assert put_response.status_code == 200
        assert put_response.json() == {"id": "1", "text": "updated todo", "done": False}

    with mock.patch.object(
            todos_routers.update_todo_use_case,
            'execute',
            return_value={"id": "1", "text": "updated todo", "done": True}
    ):
        patch_response = client.patch(
            "/todos/1",
            json={"done": True}
        )
        assert patch_response.status_code == 200
        assert patch_response.json() == {"id": "1", "text": "updated todo", "done": True}

def test_update_todos_id__with_empty_text_parameter__should_400():
    put_response = client.put(
        "/todos/1",
        json={"text": ""}
    )
    assert put_response.status_code == 400
    assert put_response.json() == {"detail": "At least one of 'text' and 'done' must be present and non empty"}

def test_update_todos_id__with_missing_parameters__should_400():
    put_response = client.put(
        "/todos/1",
        json={}
    )
    assert put_response.status_code == 400
    assert put_response.json() == {"detail": "At least one of 'text' and 'done' must be present and non empty"}

def test_update_todos_id__when_todo_doesnt_exist__should_404():
    with mock.patch.object(
        todos_routers.update_todo_use_case,
        'execute',
        return_value=None
    ):
        put_response = client.put(
            "/todos/1",
            json={"text": "some new text"}
        )
        assert put_response.status_code == 404
        assert put_response.json() == {"detail": "No item found for id: 1"}

def test_delete_todos_id__should_delete_todo():
    with mock.patch.object(
        todos_routers.delete_todo_by_id_use_case,
        'execute',
        return_value={"id": "1", "text": "some todo", "done": False}
    ):
        response = client.delete("/todos/1")
        assert response.status_code == 204
        assert response.json() == {"id": "1", "text": "some todo", "done": False}

def test_delete_todos_id__when_item_doesnt_exist__should_404():
    with mock.patch.object(
        todos_routers.delete_todo_by_id_use_case,
        'execute',
        return_value=None
    ):
        response = client.delete("/todos/1")
        assert response.status_code == 404
        assert response.json() == {"detail": "No item found for id: 1"}