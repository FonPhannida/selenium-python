from selenium.webdriver.common.by import By


class Login:

    def login(self, username, password):

        self.driver.find_element(By.CSS_SELECTOR, '#SignInNavbarLarge > li:nth-child(3) > a:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR, '#Email').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#Password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'div.form-group:nth-child(8) > div:nth-child(1) > a:nth-child(1)').click()