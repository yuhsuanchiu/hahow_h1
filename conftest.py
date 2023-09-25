import pytest
from selenium.webdriver import Chrome


@pytest.fixture(name='driver')
def create_chrome_driver() -> Chrome:
    driver = Chrome()
    yield driver
    driver.quit()
