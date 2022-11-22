from datetime import date
from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
    "nome": "cascata",
    "idade": 4
}
data_response = {}

def test_create_animals():
    response = client.post("/animals", json=data)
    data_response = response
    print(vars(response))
    assert response.status_code == 201
    assert response.json()["nome"] == data["nome"]
    assert response.json()["idade"] == data["idade"]

def test_get_all_animals():
    response = client.get("/animals", json=data)
    assert response.status_code == 200

def test_get_animals():
    response = client.get(f"/animals/{data['id']}")
    assert response.status_code == 200
    assert response.json()["nome"] == data["nome"]
    assert response.json()["idade"] == data["idade"]

def test_update_animals():
    response = client.put(f"/animals/{data['id']}", json = {
        "nome": "cascata",
        "idade": 4
    })
    assert response.status_code == 200
    assert response.json() == {   
        "nome": "cascata",
        "idade": 4
    }

def test_delete_animals():
    response = client.delete(f"/animals/{data['id']}")
    assert response.status_code == 204
    assert response.json() == {   
        "nome": "cascata",
        "idade": 4
    }