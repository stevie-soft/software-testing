from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from sites.automationexercise.common.cookie_modal import CookieModal
from sites.automationexercise.common.navbar import NavBar
from sites.automationexercise.home.home_page import HomePage
from sites.automationexercise.login.login_form import LoginForm
from sites.automationexercise.login.login_page import LoginPage
from sites.automationexercise.login.signup_form import SignupForm
from sites.automationexercise.signup.account_form import AccountForm


class AutomationExerciseWebsite:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.pages = {
            "Home": HomePage(driver),
            "Login": LoginPage(driver),
        }
        self.scopes = {
            "Navbar": NavBar(driver),
            "Account Form": AccountForm(driver),
            "Signup Form": SignupForm(driver),
            "Login Form": LoginForm(driver),
        }

        self.cookie_modal = CookieModal(driver)
        self.navbar = NavBar(driver)

    def says(self, text: str, timeout_seconds: float = 10.0) -> bool:
        xpath = f"//*[contains(text(), '{text}')]"

        try:
            WebDriverWait(self.driver, timeout_seconds).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False

    def has_cookie(self, cookie_name: str) -> bool:
        return self.driver.get_cookie(cookie_name) is not None  # type: ignore
