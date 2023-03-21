import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebdriverWrapper
from test_data.test_mouseover_product_data import test_filter_sort_data
from selenium import webdriver


class TestShoppingCart(WebdriverWrapper):
    @pytest.mark.parametrize("search_product, price_range, size", test_filter_sort_data)
    def test_shopping_cart(self, search_product, price_range, size):
        actions = webdriver.ActionChains(self.driver)
        search_bar = self.driver.find_element(By.XPATH, "//input[@placeholder='Search for products']")
        actions.send_keys_to_element(search_bar, search_product).send_keys(webdriver.Keys.ENTER).perform()
        self.driver.find_element(By.XPATH, "//button[@data-toggle='dropdown']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Price: High to Low']").click()
        actual_sort = self.driver.find_element(By.XPATH, "//button[@data-toggle='dropdown']").text
        assert_that(actual_sort.strip()).is_equal_to("Price: High to Low")
        ele_price_range = self.driver.find_element(By.XPATH, "//input[@value='500-1000']")
        self.driver.execute_script("arguments[0].click()", ele_price_range)
        ele_size = self.driver.find_element(By.XPATH, "//input[@value='6']")
        self.driver.execute_script("arguments[0].click()", ele_size)
        print(self.driver.find_element(By.XPATH, "(//span[text()='₹500.00'])[2]").text)
        time.sleep(20)


