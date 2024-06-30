import requests
from conftest import EmailGenerator
from data import DataUrls
import allure


class TestLogin:
    @allure.title('Логин под существующим пользователем')
    def test_login_old_user(self):
        user = EmailGenerator.generated_user_data()
        requests.post(DataUrls.CREATE_USER, data=user)
        response = requests.post(DataUrls.LOGIN_USER, data=user)
        assert response.status_code == 200 and '"success": true'
        requests.delete(DataUrls.BASE_URL + DataUrls.CHANGING_USER, data=user)

    @allure.title('Логин с неверным логином и паролем')
    def test_login_invalid_user_data(self):
        user1 = EmailGenerator.generated_user_data()
        user2 = EmailGenerator.generated_user_invalid_data()
        requests.post(DataUrls.CREATE_USER, data=user1)
        response = requests.post(DataUrls.LOGIN_USER, data=user2)
        assert response.status_code == 401 and '"success": false'
        requests.delete(DataUrls.BASE_URL + DataUrls.CHANGING_USER, data=user1)