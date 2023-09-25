from selenium.webdriver.chrome.webdriver import WebDriver


def get_header_bar_list(driver: WebDriver, elements: tuple, timeout: float = 3) -> list[str]:
    element_list = driver.find_elements(*elements)
    return [ele.text for ele in element_list]

