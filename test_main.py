import time
from main import get_header_bar_list
from selenium.webdriver import Chrome
from locator import HEADER_BAR

URL = 'https://www.rottentomatoes.com/'


def test_header_bar(driver: Chrome):
    expected = "MOVIES"
    driver.get(URL)
    header_bar = get_header_bar_list(driver, HEADER_BAR)
    assert expected in header_bar

