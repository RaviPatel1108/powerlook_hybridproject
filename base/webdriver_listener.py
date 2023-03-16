import pytest
from selenium import webdriver


class WebdriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.powerlook.in/")
        yield
        self.driver.quit()
