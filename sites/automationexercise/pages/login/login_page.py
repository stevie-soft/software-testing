from selenium.webdriver.remote.webdriver import WebDriver
from sites.automationexercise.pages.login.elements.signup_form import SignupForm
from sites.automationexercise.pages.webpage import (
    AutomationExerciseWebPage,
)


class LoginPage(AutomationExerciseWebPage):
    def __init__(
        self,
        driver: WebDriver,
    ) -> None:
        super().__init__(
            driver=driver,
            subpath="/login",
        )
        self.signup_form = SignupForm(driver)
