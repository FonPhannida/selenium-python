from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
from .utilibox import Login


class TestLogin(Login):
    load_dotenv()
    secret_email = os.getenv('EMAIL')
    secret_password = os.getenv('INPASSWORD')
    secret_url = os.getenv('BASE_ONLINE_URL')
    error_msg = os.getenv('LOGIN_ERR_MSG')

    def test_url(self):
        self.driver.get(self.secret_url)
        page_url = self.driver.current_url
        assert self.secret_url in page_url
        time.sleep(5)

    def test_check_login_incorrectly(self):
        self.login(self.secret_email, self.secret_password)
        web_error_msg = self.driver.find_element(By.CSS_SELECTOR, '.bootbox-body').text
        assert self.error_msg in web_error_msg
