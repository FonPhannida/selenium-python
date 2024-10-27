from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
from .utilibox import Login


class TestLogin(Login):
    load_dotenv()
    secret_email = os.getenv('EMAIL')
    secret_password = os.getenv('PASSWORD')
    secret_url = os.getenv('BASE_ONLINE_URL')
    title = os.getenv('ONLINE_TITLE')
    logout_button = os.getenv('LOGOUT_BUTTON')

    def test_url(self):
        self.driver.get(self.secret_url)

        page_url = self.driver.current_url
        assert self.secret_url in page_url
        time.sleep(5)

    def test_check_login_correctly(self):
        self.login(self.secret_email, self.secret_password)
        assert self.driver.title == self.title
        assert self.driver.find_element(By.CSS_SELECTOR,
                                   '#login > p:nth-child(1) > a:nth-child(1)').text == self.logout_button

