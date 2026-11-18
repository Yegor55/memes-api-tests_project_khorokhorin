import requests
import allure

from endpoints.endpoint import Endpoint


class CheckToken(Endpoint):

    @allure.step('Check authorization token')
    def check_token(self, token):
        self.response = requests.get(
            f'{self.url}/authorize/{token}',
            headers={'Authorization': token}
        )
