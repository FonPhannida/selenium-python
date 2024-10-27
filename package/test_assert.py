from importfile import *

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class TestWebpage:
    load_dotenv()
    #create function test case
    def test_url(self):
        driver.get(os.getenv('BASE_URL'))
        page_url = driver.current_url
        assert os.getenv('BASE_URL') in page_url


    def test_tille(self):
        assert driver.title == os.getenv('WEB_NAME')

    def test_wait(self):
        time.sleep(10)

    def test_quitbrowser(self):
        driver.quit()
