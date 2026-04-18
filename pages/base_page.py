from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configs.config import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    def open(self, url):
        self.driver.get(url)
        print("Current URL:", self.driver.current_url)

    def find(self, locator):
        # return self.wait.until(EC.presence_of_element_located(locator))
        return self.wait.until(EC.visibility_of_element_located(locator))


    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text