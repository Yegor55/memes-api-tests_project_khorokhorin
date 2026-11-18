import pytest
from pathlib import Path

from endpoints.authorize import Authorize
from endpoints.check_token import CheckToken


TOKEN_FILE = Path(__file__).parent / 'token.txt'


@pytest.fixture(scope='session')
def auth_token():
    if TOKEN_FILE.exists():
        token = TOKEN_FILE.read_text().strip()

        if token:
            check = CheckToken()
            check.check_token(token)

            if check.response.status_code == 200:
                return token

    auth = Authorize()
    token = auth.generate_token('Egor')

    assert auth.response.status_code == 200

    TOKEN_FILE.write_text(token)

    return token
