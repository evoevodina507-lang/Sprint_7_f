import allure
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"
API = f"{BASE_URL}/api/v1"


@allure.step("Отправка запроса на создание курьера")
def create_courier(payload):
    return requests.post(f"{API}/courier", json=payload, timeout=30)


@allure.step("Отправка запроса на авторизацию курьера")
def login_courier(login, password):
    return requests.post(f"{API}/courier/login", json={"login": login, "password": password}, timeout=30)


@allure.step("Отправка запроса на удаление курьера")
def delete_courier(courier_id):
    return requests.delete(f"{API}/courier/{courier_id}", timeout=30)


@allure.step("Отправка запроса на создание заказа")
def create_order(payload):
    return requests.post(f"{API}/orders", json=payload, timeout=30)


@allure.step("Отправка запроса на получение списка заказов")
def get_orders(params=None):
    return requests.get(f"{API}/orders", params=params, timeout=30)