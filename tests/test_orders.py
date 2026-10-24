import allure
import pytest
from helpers import create_order, get_orders, make_order_payload

@allure.feature("Создание заказа")
class TestOrderCreate:
    @allure.title("Создание заказа с цветом: {color}")
    @pytest.mark.parametrize(
        "color",
        [["BLACK"], ["GREY"], ["BLACK", "GREY"], []],
        ids=["BLACK", "GREY", "BLACK+GREY", "no_color"],
    )
    def test_create_order_with_colors(self, color):
        payload = make_order_payload(color=color if color else [])
        if not color:
            payload.pop("color")
        response = create_order(payload)
        assert response.status_code == 201
        body = response.json()
        assert "track" in body
        assert isinstance(body["track"], int)

@allure.feature("Список заказов")
class TestOrderList:
    @allure.title("В тело ответа возвращается список заказов")
    def test_get_orders_returns_list(self):
        response = get_orders()
        assert response.status_code == 200
        body = response.json()
        assert "orders" in body
        assert isinstance(body["orders"], list)