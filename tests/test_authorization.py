import pytest
from endpoints.authorize import Authorize
from endpoints.check_token import CheckToken


def test_successful_authorization():
    auth = Authorize()
    auth.generate_token('Egor')
    auth.check_status_code(200)
    auth.check_token_exists()
    auth.check_username('Egor')


def test_authorization_without_name():
    auth = Authorize()
    auth.generate_token(body={})

    auth.check_status_code(400)
    auth.check_response_text('Invalid parameters')


@pytest.mark.parametrize('invalid_name', [123, True, None, [], {}])
def test_authorization_with_invalid_name_type(invalid_name):
    auth = Authorize()
    auth.generate_token(body={'name': invalid_name})
    auth.check_status_code(400)
    auth.check_response_text('Invalid parameters')


def test_valid_authorization_token(auth_token):
    check = CheckToken()
    check.check_token(auth_token)

    check.check_status_code(200)
    check.check_response_text('Token is alive')


def test_invalid_authorization_token():
    check = CheckToken()
    check.check_token('invalid_token_12345')

    check.check_status_code(404)
    check.check_response_text('Token not found')
