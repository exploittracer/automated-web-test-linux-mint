from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from configs.config import Config

class LoginPage(BasePage):

    URL = Config.BASE_URL + "/login"

    USERNAME = (By.NAME, "username")

    PASSWORD = (By.NAME, "password")

    LOGIN_BTN = (By.CSS_SELECTOR , "button.mantine-focus:nth-child(5)")

    DASHBOARD_TEXT = (By.TAG_NAME, "h2")

    def load(self):
        self.open(self.URL)
        assert "login" in self.driver.current_url.lower()

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        print("Username", username)
        print("Password", password)
        self.click(self.LOGIN_BTN)

    def get_dashboard_text(self):
        return self.get_text(self.DASHBOARD_TEXT)