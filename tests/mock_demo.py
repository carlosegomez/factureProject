import requests
import responses
import unittest
from dataclasses import dataclass


@dataclass
class User:
    first_name: str = ''
    last_name: str = ''
    email: str = ''
    user_name: str = ''

    @classmethod
    def create_from_api(cls, result):
        record = result['results'][0]
        return cls(record['name']['first'], record['name']['last'], record['email'], record['login']['username'])


class APIDisconnectException(Exception):
    pass


class HttpNotFoundException(Exception):
    pass


def get_user():
    try:
        response = requests.get('https://randomuser.me/api/')

        if response.status_code == 404:
            raise HttpNotFoundException()

        return User.create_from_api(response.json())
    except requests.exceptions.ConnectionError:
        raise APIDisconnectException()


class GetUserTest(unittest.TestCase):

    USER_MOCK = {
        'results': [{
            'name': dict(title='ms', first='mabel', last='fleming'),
            'email': 'mabel.fleming@example.com',
            'login': dict(username='heavyfrog837')
        }]
    }

    @unittest.skip
    @responses.activate
    def test_response_ok(self):
        responses.add(responses.GET, 'https://randomuser.me/api/', json=self.USER_MOCK)
        user = get_user()
        self.assertIsInstance(user, User)
        self.assertEqual(user.first_name, 'mabel')

    @unittest.skip
    @responses.activate
    def test_response_ko(self):
        responses.add(responses.GET, 'https://randomuser.me/api/', status=404)
        with self.assertRaises(HttpNotFoundException):
            get_user()

    @unittest.skip
    @responses.activate
    def test_connection_ko(self):
        with self.assertRaises(APIDisconnectException):
            get_user()


if __name__ == '__main__':
    unittest.main()
    # try:
    #     user = get_user('https://randomuser.me/api/')
    #     print(user)
    # except APIDisconnectException:
    #     print('Connection error')
    # except HttpNotFoundException:
    #     print('Address not found')



