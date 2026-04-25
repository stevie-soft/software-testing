from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebPageElement:
    def __init__(
        self,
        driver: WebDriver,
        reference: str,
        selector: str,
        timeout_seconds: float = 10.0,
    ) -> None:
        self.reference = reference
        self.locator = (By.CSS_SELECTOR, selector)
        self.__driver = driver
        self.__timeout_seconds = timeout_seconds
        self.__wait = WebDriverWait(self.__driver, timeout=timeout_seconds)

    @property
    def text(self) -> str:
        return self.__element.text

    def click(self):
        self.__element.click()

    def fill(self, text: str | int | float, /, *, replace: bool = True):
        if replace:
            self.__element.clear()

        self.__element.send_keys(str(text))

    @property
    def __element(self) -> WebElement:
        self.__wait_until_visible()

        try:
            return self.__driver.find_element(*self.locator)
        except NoSuchElementException:
            [by_type, by_value] = self.locator
            raise Exception(
                f"Cannot find element(s) with '{by_type}' of '{by_value}'. "
            )

    def __wait_until_visible(self) -> None:
        try:
            self.__wait.until(EC.visibility_of_element_located(self.locator))
        except TimeoutException:
            [by_type, by_value] = self.locator
            raise Exception(
                f"Cannot locate element(s) with '{by_type}' of '{by_value}' in {self.__timeout_seconds} seconds. "
            )
