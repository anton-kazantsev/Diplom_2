import requests
from conftest import EmailGenerator
from data import DataUrls
from helpers import burger1
from helpers import burger2
from helpers import burger3
import allure


class TestCreateOrder:
    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_authorization(self):
        user = EmailGenerator.generated_user_data()
        burger = burger1
        requests.post(DataUrls.CREATE_USER, data=user)
        requests.get(DataUrls.LOGIN_USER, data=user)
        response = requests.post(DataUrls.CREATE_ORDER, data=burger)
        assert response.status_code == 200 and '"success": true'
        requests.delete(DataUrls.BASE_URL + DataUrls.CHANGING_USER, data=user)

    @allure.title('Создание заказа без авторизации')
    def test_create_order_not_authorization(self):
        burger = burger1
        response = requests.post(DataUrls.CREATE_ORDER, data=burger)
        assert response.status_code == 200 and '"success": true'

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_not_ingredient(self):
        user = EmailGenerator.generated_user_data()
        burger = burger2
        requests.post(DataUrls.CREATE_USER, data=user)
        requests.get(DataUrls.LOGIN_USER, data=user)
        response = requests.post(DataUrls.CREATE_ORDER, data=burger)
        assert response.status_code == 400 and '"success": false'
        requests.delete(DataUrls.BASE_URL + DataUrls.CHANGING_USER, data=user)

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredient(self):
        user = EmailGenerator.generated_user_data()
        burger = burger3
        requests.post(DataUrls.CREATE_USER, data=user)
        requests.get(DataUrls.LOGIN_USER, data=user)
        response = requests.post(DataUrls.CREATE_ORDER, data=burger)
        assert response.status_code == 500 and '"success": false'
        requests.delete(DataUrls.BASE_URL + DataUrls.CHANGING_USER, data=user)