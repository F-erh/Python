import requests


def test_get():
     response = requests.get("http://localhost:8000/animals")
     assert response.status_code == 200

     assert response.headers["Content-Type"] == "application/json"