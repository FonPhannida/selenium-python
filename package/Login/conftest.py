

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#headless chrome
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(autouse=True, scope='class')
def setup(request):
    options = Options()
    options.add_argument('--headless')
    #normal browder
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #headless is mean browser will not sure run step on moniter
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    request.cls.driver = driver

    yield
    driver.quit()