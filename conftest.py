import pytest
from selenium import webdriver
from configs.config import Config

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()

    if Config.HEADLESS:
        options.add_argument("--headless")

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(Config.TIMEOUT)

    yield driver

    driver.quit()