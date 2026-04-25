from selenium.webdriver.remote.webdriver import WebDriver
from sites.automationexercise.pages.webpage import (
    AutomationExerciseWebPage,
)


class HomePage(AutomationExerciseWebPage):
    def __init__(
        self,
        driver: WebDriver,
    ) -> None:
        super().__init__(
            driver=driver,
            subpath="/",
        )
