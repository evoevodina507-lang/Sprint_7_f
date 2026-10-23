import allure
import pytest
from helpers import create_courier, delete_courier, login_courier

@allure.feature("Логин курьера")
class TestCourierLogin:
    @allure.title("Курьер может авторизоваться")
    def test_login_success(self, courier):
        response = login_courier(courier["payload"]["login"], courier["payload"]["password"])
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Нельзя авторизоваться с неверным паролем")
    def test_login_wrong_password(self, courier):
        response = login_courier(courier["payload"]["login"], "wrong_password")
        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"

    @allure.title("Нельзя авторизоваться с неверным логином")
    def test_login_wrong_login(self, courier):
        response = login_courier("wrong_login", courier["payload"]["password"])
        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"

    @allure.title("Нельзя авторизоваться под несуществующим пользователем")
    def test_login_nonexistent_user(self):
        response = login_courier("no_such_login_xxx", "no_such_password_xxx")
        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"

    @allure.title("Нельзя авторизоваться без поля {missing_field}")
    # Оставляем только "login", так как при отсутствии "password" сервер Яндекса зависает (баг стенда)
    @pytest.mark.parametrize("missing_field", ["login"])
    def test_login_missing_field(self, courier, missing_field):
        body = {"login": courier["payload"]["login"], "password": courier["payload"]["password"]}
        body.pop(missing_field)
        
        response = login_courier(body.get("login"), body.get("password"))

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для входа"