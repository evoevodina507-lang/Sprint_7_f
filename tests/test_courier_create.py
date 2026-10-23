import allure
import pytest
from helpers import create_courier, delete_courier, login_courier, make_courier_payload

@allure.feature("Создание курьера")
class TestCourierCreate:
    @allure.title("Курьера можно создать")
    def test_create_courier_success(self):
        payload = make_courier_payload()
        response = create_courier(payload)
        try:
            assert response.status_code == 201
            assert response.json() == {"ok": True}
        finally:
            login_response = login_courier(payload["login"], payload["password"])
            if login_response.ok:
                delete_courier(login_response.json()["id"])

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, courier):
        response = create_courier(courier["payload"])
        assert response.status_code == 409
        assert response.json().get("message") == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Нельзя создать курьера без поля {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_field(self, missing_field):
        payload = make_courier_payload()
        payload.pop(missing_field)
        response = create_courier(payload)
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"