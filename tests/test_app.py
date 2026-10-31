import pytest
from app import app, accounts

@pytest.fixture()
def client():
    accounts.clear()
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_create_read_list_update_delete(client):
    created = client.post("/accounts", json={"name": "Ada Lovelace", "email": "ada@example.com"})
    assert created.status_code == 201
    account_id = created.json["id"]
    assert client.get(f"/accounts/{account_id}").json["name"] == "Ada Lovelace"
    assert len(client.get("/accounts").json) == 1
    updated = client.put(f"/accounts/{account_id}", json={"name": "Ada Byron"})
    assert updated.status_code == 200
    assert updated.json["name"] == "Ada Byron"
    assert client.delete(f"/accounts/{account_id}").status_code == 204
    assert client.get(f"/accounts/{account_id}").status_code == 404

def test_create_requires_fields(client):
    assert client.post("/accounts", json={"name": "Missing email"}).status_code == 400
