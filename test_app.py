from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD!"}



def test_add_endpoint():
    response = client.get("/add?a=4&b=6")
    assert response.status_code == 200
    assert response.json() == {"result": 10}