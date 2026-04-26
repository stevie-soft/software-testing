from typing import Literal

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class DomElement:
    def __init__(
        self,
        _type: Literal["input", "button", "select", "h2"],
        _attributes: dict[str, str],
        /,
    ) -> None:
        self.locator = (
            By.CSS_SELECTOR,
            f"{_type}{self.__attributes_as_selector(_attributes)}",
        )

    @staticmethod
    def __attributes_as_selector(attributes: dict[str, str]) -> str:
        selector = ""

        for key, value in attributes.items():
            selector += f'[{key}="{value}"]'

        return selector


class _HtmlUtils:
    def __init__(
        self,
        driver: WebDriver,
        default_timeout_seconds: float = 10.0,
    ) -> None:
        self.driver = driver
        self.__wait = WebDriverWait(driver, default_timeout_seconds)

    def find_visible(self, dom_elem: DomElement) -> WebElement:
        return self.__wait.until(EC.visibility_of_element_located(dom_elem.locator))

    def find_clickable(self, dom_elem: DomElement) -> WebElement:
        return self.__wait.until(EC.element_to_be_clickable(dom_elem.locator))

    def is_clickable(self, dom_elem: DomElement) -> bool:
        try:
            self.find_clickable(dom_elem)
            return True
        except TimeoutException:
            return False

    def click_on(self, dom_elem: DomElement) -> None:
        web_elem = self.find_clickable(dom_elem)
        web_elem.click()

    def fill(self, dom_elem: DomElement, value: str | int | float) -> None:
        self.type_into(dom_elem, value, replace=True)

    def has_cookie(self, cookie_name: str) -> bool:
        return self.driver.get_cookie(cookie_name) is not None  # type: ignore

    def set_option_by_value(self, dom_elem: DomElement, option_value: str) -> None:
        select = Select(self.find_visible(dom_elem))
        select.select_by_value(option_value)

    def set_option_by_text(self, dom_elem: DomElement, option_value: str) -> None:
        select = Select(self.find_visible(dom_elem))
        select.select_by_visible_text(option_value)

    def type_into(
        self,
        dom_elem: DomElement,
        value: str | int | float,
        replace: bool = False,
    ) -> None:
        web_elem = self.find_visible(dom_elem)

        if replace:
            web_elem.clear()

        web_elem.send_keys(str(value))


class HtmlElement:
    def __init__(self, driver: WebDriver) -> None:
        self.html = _HtmlUtils(driver)


class HtmlForm(HtmlElement):
    FIELDS = {}
    BUTTONS = {}


class WebPage(HtmlElement):
    URL = ""
    SUBPATH = ""

    def visit(self):
        self.html.driver.get(f"{self.URL}/{self.SUBPATH}")
