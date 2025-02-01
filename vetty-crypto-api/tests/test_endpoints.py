from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_coins():
    response = client.get("/api/v1/coins", headers={"X-API-Key": "your_api_key_here"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_coin():
    response = client.get("/api/v1/coins/bitcoin", headers={"X-API-Key": "your_api_key_here"})
    assert response.status_code == 200
    assert "id" in response.json()


def test_list_coins_invalid_api_key():
    response = client.get("/api/v1/coins", headers={"X-API-Key": "invalid_key"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid API Key"}
