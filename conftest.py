import pytest
from helpers import create_courier, delete_courier, login_courier, make_courier_payload

@pytest.fixture
def courier():
    payload = make_courier_payload()
    response = create_courier(payload)
    assert response.status_code == 201, f"Не удалось создать курьера: {response.text}"

    login_response = login_courier(payload["login"], payload["password"])
    courier_id = login_response.json().get("id") if login_response.ok else None

    yield {"payload": payload, "id": courier_id}

    if courier_id is not None:
        delete_courier(courier_id)
