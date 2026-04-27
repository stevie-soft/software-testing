from typing import Literal

from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By, ByType
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

type DomElementMeta = tuple[
    Literal["input", "button", "select", "a", "p"],
    dict[str, str],
]


def _meta_as_selector(meta: DomElementMeta) -> str:
    [tag_name, tag_attributes] = meta

    selector = tag_name

    for key, value in tag_attributes.items():
        selector += f'[{key}="{value}"]'

    return selector


class DomElement:
    def __init__(
        self,
        driver: WebDriver,
        matcher: str,
        matcher_type: ByType = By.CSS_SELECTOR,
        timeout_seconds: float = 10.0,
    ) -> None:
        self.__wait = WebDriverWait(
            driver,
            timeout_seconds,
            ignored_exceptions=(StaleElementReferenceException,),
        )
        self.__locator = (
            matcher_type,
            matcher,
        )

    def fill(self, value: str) -> None:
        self.send_keys(value, replace=True)

    def send_keys(
        self,
        value: str | int | float,
        replace: bool = False,
    ) -> None:
        if replace:
            self.__as_visible_web_element.clear()

        self.__as_visible_web_element.send_keys(str(value))

    def click(self) -> None:
        self.__as_clickable_web_element.click()

    def set(self, value: str) -> None:
        self.__as_select_web_element.select_by_visible_text(value)

    def says(self, value: str) -> bool:
        return self.__wait.until(lambda _: value.lower() in self.text.lower())

    @property
    def text(self) -> str:
        return self.__as_visible_web_element.text

    def is_visible(self) -> bool:
        try:
            self.__as_visible_web_element
            return True
        except TimeoutException:
            return False

    def is_clickable(self) -> bool:
        try:
            self.__as_clickable_web_element
            return True
        except TimeoutException:
            return False

    @property
    def __as_visible_web_element(self) -> WebElement:
        return self.__wait.until(EC.visibility_of_element_located(self.__locator))

    @property
    def __as_clickable_web_element(self) -> WebElement:
        return self.__wait.until(EC.element_to_be_clickable(self.__locator))

    @property
    def __as_select_web_element(self) -> Select:
        return Select(self.__as_visible_web_element)


class HtmlElement:
    ELEMENTS: dict[str, DomElementMeta] = {}

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.elements: dict[str, DomElement] = {}

        for ref, meta in self.ELEMENTS.items():
            self.elements[ref] = DomElement(
                driver=driver,
                matcher=_meta_as_selector(meta),
            )


class WebPage(HtmlElement):
    URL = ""
    SUBPATH = ""

    def visit(self):
        self.driver.get(f"{self.URL}/{self.SUBPATH}")
