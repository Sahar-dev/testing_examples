# to run : pytest fastapi/test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_greet():
    response = client.get("/greet/John")
    assert response.status_code == 200
    # Valid test
    # assert response.json() == {"message": "Hello, John!"}
    # Invalid test
    assert response.json() == {"message": "Hello, Sahar!"}
