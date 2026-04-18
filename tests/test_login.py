import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("admin", "Frosted-Glutinous-Disobey-Simmering-Shown5-Dill-Hypnosis-Carol-Mom-Unusual")

    assert "Dashboard" in login_page.get_dashboard_text()