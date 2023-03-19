import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebdriverWrapper
from test_data.test_mouseover_product_data import test_shopping_cart_data
from selenium import webdriver


class TestShoppingCart(WebdriverWrapper):
    @pytest.mark.parametrize("category_name,subcategory_name,product_size,empty_bag_message", test_shopping_cart_data
                             )
    def test_shopping_cart(self, category_name, subcategory_name, product_size, empty_bag_message):
        actions = webdriver.ActionChains(self.driver)
        actions.move_to_element(
                self.driver.find_element(By.XPATH, f"//a[normalize-space()='{category_name}']")).perform()
        self.driver.find_element(By.XPATH, f"//span[normalize-space()='{subcategory_name}']").click()
        self.driver.find_element(By.XPATH, "//img[contains(@src, 'a355f488ce208bb58a90660f35cdc6e0')][1]").click()
        self.driver.find_element(By.XPATH, f"(//span[normalize-space()='{product_size}'])[2]").click()
        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Add to Bag'])[2]").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='VIEW BAG']").is_displayed()
        self.driver.find_element(By.CLASS_NAME, "icon-cart1").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Checkout']").is_displayed()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Remove']").click()
        actual_message = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Your bag is empty.']").text
        assert_that(actual_message).is_equal_to(empty_bag_message)
