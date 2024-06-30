import random
import string


class EmailGenerator:

    @classmethod
    def generated_user_data(cls):
        def random_email():
            return 'antonkazantcev' + ''.join(random.choice(string.ascii_letters) for _ in range(99)) + "@yandex.ru"

        email = random_email()
        password = '12345678'
        name = 'Антон'

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        return payload

    @classmethod
    def generated_user_data_not_password(cls):
        def random_email():
            return 'antonkazantcev' + ''.join(random.choice(string.ascii_letters) for _ in range(99)) + "@yandex.ru"

        email = random_email()
        name = 'Антон'

        payload = {
            "email": email,
            "name": name
        }

        return payload

    @staticmethod
    def generated_user_invalid_data():
        email = 'kazantcevanton@ya.ru'
        password = '87654321'
        name = 'Антон'

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        return payload