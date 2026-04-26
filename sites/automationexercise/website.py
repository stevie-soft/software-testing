from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from sites.automationexercise.common.cookie_modal import CookieModal
from sites.automationexercise.home.home_page import HomePage
from sites.automationexercise.login.login_form import LoginForm
from sites.automationexercise.login.login_page import LoginPage
from sites.automationexercise.login.signup_form import SignupForm
from sites.automationexercise.signup.account_form import AccountForm


class AutomationExerciseWebsite:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.cookie_modal = CookieModal(driver)
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)
        self.login_form = LoginForm(driver)
        self.signup_form = SignupForm(driver)
        self.account_form = AccountForm(driver)

    def says(self, text: str, timeout_seconds: float = 10.0) -> bool:
        xpath = f"//*[contains(normalize-space(.), '{text}')]"

        try:
            WebDriverWait(self.driver, timeout_seconds).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False
