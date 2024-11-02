import time

from selenium.webdriver.common.by import By
from .utilibox import Login


class TestLandingPage(Login):

    def test_landing_page(self):
        self.test_url()
        landing_page_test = self.driver.find_element(By.CSS_SELECTOR, '#SignInNavbarLarge > li:nth-child(3) > a:nth-child(1)').text
        print(landing_page_test)
        assert landing_page_test == 'Sign In'

    def test_version(self):
        self.driver.find_element(By.CSS_SELECTOR, '#SignInNavbarLargeSearch > a:nth-child(1) > span:nth-child(1)').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'button.pull-left').click()
        search_text_result = self.driver.find_element(By.CSS_SELECTOR, 'td.text-center:nth-child(1) > span:nth-child(1)').text
        print(search_text_result)
        assert search_text_result == 'Saturday'

    # def test_login_admin(self):
    #     self.test_url()
    #     self.driver.find_element(By.CSS_SELECTOR, '#SignInNavbarLarge > li:nth-child(3) > a:nth-child(1)').click()
    #     time.sleep(2)
    #     self.driver.find_element(By.CSS_SELECTOR, '#Email').send_keys('<EMAIL>')
    #     self.driver.find_element(By.CSS_SELECTOR, '#Password').send_keys('<PASSWORD>')
    #     self.driver.find_element(By.CSS_SELECTOR, '#div.form-group:nth-child(8) > div:nth-child(1) > a:nth-child(1)').click()

    #test