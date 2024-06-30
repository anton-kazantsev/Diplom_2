import requests
from conftest import EmailGenerator
from data import DataUrls
import allure


class TestChangeUserData:
    @allure.title('Изменение данных пользователя с авторизацией')
    def test_change_user_data_with_authorization(self):
        user = EmailGenerator.generated_user_data()
        user1 = EmailGenerator.generated_user_data()
        requests.post(DataUrls.CREATE_USER, data=user)
        login = requests.post(DataUrls.LOGIN_USER, data=user)
        id_user = login.json()["accessToken"]
        response = requests.get(DataUrls.CHANGING_USER, headers={"Authorization": id_user}, data=user1)
        assert response.status_code == 200 and '"success": true'
        requests.delete(DataUrls.BASE_URL + DataUrls.CHANGING_USER, data=user)

    @allure.title('Изменение данных пользователя без авторизации')
    def test_change_user_data_not_authorization(self):
        user = EmailGenerator.generated_user_data()
        user1 = EmailGenerator.generated_user_data()
        requests.post(DataUrls.CREATE_USER, data=user)
        response = requests.get(DataUrls.CHANGING_USER, data=user1)
        assert response.status_code == 401 and '"success": false'
        requests.delete(DataUrls.BASE_URL + DataUrls.CHANGING_USER, data=user)