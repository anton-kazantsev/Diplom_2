import requests
from conftest import EmailGenerator
from data import DataUrls
from helpers import burger1
import allure


class TestReceivingOrders:
    @allure.title('Получение заказов авторизированного пользователя')
    def test_receiving_orders_with_authorization(self):
        user = EmailGenerator.generated_user_data()
        burger = burger1
        requests.post(DataUrls.CREATE_USER, data=user)
        requests.get(DataUrls.LOGIN_USER, data=user)
        requests.post(DataUrls.CREATE_ORDER, data=burger)
        login = requests.post(DataUrls.LOGIN_USER, data=user)
        id_user = login.json()["accessToken"]
        response = requests.get(DataUrls.CREATE_ORDER, headers={"Authorization": id_user}, data=user)
        assert response.status_code == 200 and '"success": true'
        requests.delete(DataUrls.BASE_URL + DataUrls.CHANGING_USER, data=user)


    @allure.title('Получение заказов неавторизированного пользователя')
    def test_receiving_order_not_authorization(self):
        burger = burger1
        requests.post(DataUrls.CREATE_ORDER, data=burger)
        response = requests.get(DataUrls.ALL_ORDER)
        assert response.status_code == 200 and '"success": true'