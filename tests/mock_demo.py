import requests
import responses
import unittest

from dataclasses import dataclass
from unittest import mock


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


USER_MOCK = {
    'results': [{
        'name': dict(title='ms', first='mabel', last='fleming'),
        'email': 'mabel.fleming@example.com',
        'login': dict(username='heavyfrog837')
    }]
}


@unittest.skip
class GetUserInternalTest(unittest.TestCase):

    @responses.activate
    def test_response_ok(self):
        responses.add(responses.GET, 'https://randomuser.me/api/', json=USER_MOCK)
        user = get_user()
        self.assertIsInstance(user, User)
        self.assertEqual(user.first_name, 'mabel')
        self.assertEqual(user.last_name, 'fleming')

    @responses.activate
    def test_response_ko(self):
        responses.add(responses.GET, 'https://randomuser.me/api/', status=404)
        with self.assertRaises(HttpNotFoundException):
            get_user()

    @responses.activate
    def test_connection_ko(self):
        with self.assertRaises(APIDisconnectException):
            get_user()


class GetUserTest(unittest.TestCase):

    @mock.patch('mock_demo.get_user')
    def test(self, mock_get_user):
        mock_get_user.return_value = User.create_from_api(USER_MOCK)
        user = get_user()
        self.assertEqual(user.first_name, 'mabel')
        self.assertEqual(user.last_name, 'fleming')


if __name__ == '__main__':
    unittest.main()
    # try:
    #     user = get_user('https://randomuser.me/api/')
    #     print(user)
    # except APIDisconnectException:
    #     print('Connection error')
    # except HttpNotFoundException:
    #     print('Address not found')



