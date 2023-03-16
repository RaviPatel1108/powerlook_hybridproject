import pytest
from base.webdriver_listener import WebdriverWrapper
from assertpy import assert_that
from test_data.test_page_details_data import test_mouseoverdata
from selenium.webdriver.common.by import By
from selenium import webdriver


class TestMouseoverProduct(WebdriverWrapper):
    @pytest.mark.parametrize("category_name, subcategory_name", test_mouseoverdata
                             )
    def test_mouseover_product(self, category_name, subcategory_name):
        actions = webdriver.ActionChains(self.driver)
        # actions.move_to_element(self.driver.find_element(By.XPATH, "//a[normalize-space()='Shirts']")).perform()
        # actual_subproduct = self.driver.find_element(By.XPATH, "//span[normalize-space()='Oversized Shirts']").text
        actions.move_to_element(self.driver.find_element(By.XPATH, f"//a[normalize-space()='{category_name}']")).perform()
        actual_subcategory_name = self.driver.find_element(By.XPATH, f"//span[normalize-space()='{subcategory_name}']").text
        assert_that(actual_subcategory_name).is_equal_to(subcategory_name)
