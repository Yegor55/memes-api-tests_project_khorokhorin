import allure


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'

    def __init__(self):
        self.response = None
        self.response_json = None

    @allure.step('Check response status code')
    def check_status_code(self, expected_code):
        assert self.response.status_code == expected_code, (
            f'Expected {expected_code}, '
            f'but got {self.response.status_code}'
        )

    @allure.step('Check response contains expected text')
    def check_response_text(self, expected_text):
        assert expected_text in self.response.text, (
            f'Expected text "{expected_text}" '
            f'not found in response: {self.response.text}'
        )
