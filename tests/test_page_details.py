import pytest
from base.webdriver_listener import WebdriverWrapper
from assertpy import assert_that
from test_data.test_page_details_data import test_page_details_data


class TestPageDetails(WebdriverWrapper):
    @pytest.mark.parametrize("expected_url, expected_title", test_page_details_data
                             )
    def test_page_details(self, expected_url, expected_title):
        actual_url = self.driver.current_url
        actual_title = self.driver.title
        assert_that(expected_url).is_equal_to(actual_url)
        assert_that(expected_title).is_equal_to(actual_title)