import requests
from conftest import EmailGenerator
from data import DataUrls
import allure


class TestNewUser:
    @allure.title('Создание пользователя')
    def test_create_new_user(self):
        user = EmailGenerator.generated_user_data()
        response = requests.post(DataUrls.CREATE_USER, data=user)
        assert response.status_code == 200 and "accessToken" in response.json()
        requests.delete(DataUrls.BASE_URL + DataUrls.CHANGING_USER, data=user)

    @allure.title('Создание пользователя с существующими данными')
    def test_create_old_user(self):
        user = EmailGenerator.generated_user_data()
        requests.post(DataUrls.CREATE_USER, data=user)
        response = requests.post(DataUrls.CREATE_USER, data=user)
        assert response.status_code == 403 and '"success": false'
        requests.delete(DataUrls.BASE_URL + DataUrls.CHANGING_USER, data=user)

    @allure.title('Создание пользователя без пароля')
    def test_create_new_user_without_password(self):
        user = EmailGenerator.generated_user_data_not_password()
        response = requests.post(DataUrls.CREATE_USER, data=user)
        assert response.status_code == 403 and '"success": false'
        requests.delete(DataUrls.BASE_URL + DataUrls.CHANGING_USER, data=user)

