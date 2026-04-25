from core import WebPageElement
from selenium.webdriver.remote.webdriver import WebDriver


class SignupForm:
    def __init__(self, driver: WebDriver) -> None:
        self.name_field = WebPageElement(
            driver=driver,
            reference="Signup name",
            selector='input[data-qa="signup-name"]',
        )
        self.email_field = WebPageElement(
            driver=driver,
            reference="Signup email",
            selector='input[data-qa="signup-email"]',
        )
        self.signup_button = WebPageElement(
            driver=driver,
            reference="Signup button",
            selector='button[data-qa="signup-button"]',
        )

    def initiate_signup(self, name: str, email: str) -> None:
        self.name_field.fill(name)
        self.email_field.fill(email)
        self.signup_button.click()
