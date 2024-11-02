from selenium.webdriver.common.by import By
import time
from .utilibox import Login


class TestLogin(Login):


    def test_check_login_correctly(self):
        self.test_url()
        self.login(self.secret_email, self.secret_password)
        assert self.driver.title == self.title
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        '#login > p:nth-child(1) > a:nth-child(1)').text == self.logout_button

