import allure
import pytest
from helpers import make_courier_payload
from api_methods import create_courier, delete_courier, login_courier
from data import MSG_COURIER_CREATED, MSG_LOGIN_BUSY, MSG_NOT_ENOUGH_DATA_CREATE


@allure.feature("Создание курьера")
class TestCourierCreate:
    @allure.title("Курьера можно создать")
    def test_create_courier_success(self):
        payload = make_courier_payload()
        response = create_courier(payload)

        assert response.status_code == 201
        assert response.json() == MSG_COURIER_CREATED

        login_response = login_courier(payload["login"], payload["password"])
        delete_courier(login_response.json()["id"])

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, courier):
        response = create_courier(courier["payload"])
        assert response.status_code == 409
        assert response.json().get("message") == MSG_LOGIN_BUSY

    @allure.title("Нельзя создать курьера без поля {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_field(self, missing_field):
        payload = make_courier_payload()
        payload.pop(missing_field)
        response = create_courier(payload)
        assert response.status_code == 400
        assert response.json().get("message") == MSG_NOT_ENOUGH_DATA_CREATE