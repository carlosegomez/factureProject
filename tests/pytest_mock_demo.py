import pytest
import requests
import responses

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


USER_MOCK = {
    'results': [{
        'name': dict(title='ms', first='mabel', last='fleming'),
        'email': 'mabel.fleming@example.com',
        'login': dict(username='heavyfrog837')
    }]
}


@responses.activate
def test_response_ok():
    responses.add(responses.GET, 'https://randomuser.me/api/', json=USER_MOCK)
    user = get_user()
    assert isinstance(user, User)
    assert user.first_name == 'mabel'
    assert user.last_name == 'fleming'


@responses.activate
def test_response_ko():
    responses.add(responses.GET, 'https://randomuser.me/api/', status=404)
    with pytest.raises(HttpNotFoundException):
        get_user()


@responses.activate
def test_connection_ko():
    with pytest.raises(APIDisconnectException):
        get_user()


def test(mocker):
    mock_user = User.create_from_api(USER_MOCK)
    mocker.patch('tests.pytest_mock_demo.get_user', return_value=mock_user)
    user = get_user()
    assert user.first_name == 'mabel'
    assert user.last_name == 'fleming'

#
# if __name__ == '__main__':
#     pass
    # unittest.main()
    # try:
    #     user = get_user('https://randomuser.me/api/')
    #     print(user)
    # except APIDisconnectException:
    #     print('Connection error')
    # except HttpNotFoundException:
    #     print('Address not found')



