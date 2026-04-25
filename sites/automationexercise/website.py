from selenium.webdriver.remote.webdriver import WebDriver

from sites.automationexercise.pages.home.home_page import HomePage
from sites.automationexercise.pages.login.login_page import LoginPage


class AutomationExerciseWebsite:
    def __init__(self, driver: WebDriver) -> None:
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)
