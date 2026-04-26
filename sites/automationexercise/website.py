from selenium.webdriver.remote.webdriver import WebDriver

from sites.automationexercise.common.cookie_modal import CookieModal
from sites.automationexercise.home.home_page import HomePage
from sites.automationexercise.login.login_form import LoginForm
from sites.automationexercise.login.login_page import LoginPage
from sites.automationexercise.login.signup_form import SignupForm
from sites.automationexercise.signup.account_form import AccountForm


class AutomationExerciseWebsite:
    def __init__(self, driver: WebDriver) -> None:
        self.cookie_modal = CookieModal(driver)
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)
        self.login_form = LoginForm(driver)
        self.signup_form = SignupForm(driver)
        self.account_form = AccountForm(driver)
