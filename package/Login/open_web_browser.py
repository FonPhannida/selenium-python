from importfile import *

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_url():
    driver.get(os.getenv('BASE_ONLINE_URL'))
    page_url = driver.current_url
    assert os.getenv('BASE_ONLINE_URL') in page_url
    time.sleep(5)
