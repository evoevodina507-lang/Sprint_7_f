import random
import string
import allure
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"
API = f"{BASE_URL}/api/v1"

# Константы с текстами сообщений (вынесены по просьбе ревьюера)
MSG_COURIER_CREATED = {"ok": True}
MSG_LOGIN_BUSY = "Этот логин уже используется. Попробуйте другой."
MSG_NOT_ENOUGH_DATA_CREATE = "Недостаточно данных для создания учетной записи"
MSG_NOT_FOUND = "Учетная запись не найдена"
MSG_NOT_ENOUGH_DATA_LOGIN = "Недостаточно данных для входа"


def generate_random_string(length=10):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def make_courier_payload():
    # Убрана логика or, функция просто возвращает данные
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string(),
    }


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


def make_order_payload(color=None):
    payload = {
        "firstName": "Тест",
        "lastName": "Курьер",
        "address": "Москва, тестовый адрес, 1",
        "metroStation": 4,
        "phone": "+7 800 555-35-35",
        "rentTime": 2,
        "deliveryDate": "2026-12-31",
        "comment": "Автотест Sprint 7",
    }
    if color is not None:
        payload["color"] = color
    return payload