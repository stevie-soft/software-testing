from core.webpage import WebPage
from selenium.webdriver.remote.webdriver import WebDriver


class AutomationExerciseWebPage(WebPage):
    def __init__(
        self,
        driver: WebDriver,
        subpath: str,
        base_url: str = "https://automationexercise.com",
    ) -> None:
        super().__init__(
            driver=driver,
            url=f"{base_url}{subpath}",
        )
