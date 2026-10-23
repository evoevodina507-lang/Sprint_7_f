import random
import string
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"
API = f"{BASE_URL}/api/v1"

def generate_random_string(length=10):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

def make_courier_payload(login=None, password=None, first_name=None):
    return {
        "login": login or generate_random_string(),
        "password": password or generate_random_string(),
        "firstName": first_name or generate_random_string(),
    }

def create_courier(payload):
    return requests.post(f"{API}/courier", json=payload, timeout=30)

def login_courier(login, password):
    return requests.post(f"{API}/courier/login", json={"login": login, "password": password}, timeout=30)

def delete_courier(courier_id):
    return requests.delete(f"{API}/courier/{courier_id}", timeout=30)

def create_order(payload):
    return requests.post(f"{API}/orders", json=payload, timeout=30)

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