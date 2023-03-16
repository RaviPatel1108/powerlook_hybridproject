import pytest
from base.webdriver_listener import WebdriverWrapper
from assertpy import assert_that
from test_data.test_page_details_data import test_invalid_signup_data
from selenium.webdriver.common.by import By


class TestInvalidSignup(WebdriverWrapper):
    @pytest.mark.parametrize("valid_name, invalid_phone, expected_error", test_invalid_signup_data
                             )
    def test_invalid_signup(self, valid_name, invalid_phone, expected_error):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Sign up Now']").click()
        self.driver.find_element(By.NAME, "name").send_keys(valid_name)
        self.driver.find_element(By.NAME, "mobile_number").send_keys(invalid_phone)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Continue']").click()
        actual_error = self.driver.find_element(By.XPATH, "//span[contains(text(),'Invalid')]").text
        assert_that(expected_error).is_equal_to(actual_error)