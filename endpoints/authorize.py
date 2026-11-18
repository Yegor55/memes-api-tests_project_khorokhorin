import requests
import allure

from endpoints.endpoint import Endpoint


class Authorize(Endpoint):
    @allure.step('Generate authorization token')
    def generate_token(self, name=None, body=None):
        if body is None:
            body = {'name': name}

        self.response = requests.post(
            f'{self.url}/authorize',
            json=body
        )
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.response_json = {}

        return self.response_json.get('token')

    @allure.step('Check authorization token exists')
    def check_token_exists(self):

        assert self.response_json.get('token')

    @allure.step('Check authorized username')
    def check_username(self, expected_name):

        assert self.response_json['user'] == expected_name
