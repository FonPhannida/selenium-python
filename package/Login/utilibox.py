import os

import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By


class Login:
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

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '#SignInNavbarLarge > li:nth-child(3) > a:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR, '#Email').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#Password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'div.form-group:nth-child(8) > div:nth-child(1) > a:nth-child(1)').click()
