import random
import string


def generate_random_string(length=10):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def make_courier_payload():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string(),
    }


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