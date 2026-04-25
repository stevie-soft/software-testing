from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class WebPage:

    def __init__(
        self, driver: WebDriver, url: str, default_timeout_seconds: int = 10
    ) -> None:
        self._driver = driver
        self._url = url
        self._wait = WebDriverWait(self._driver, default_timeout_seconds)
        self._default_timeout_seconds = default_timeout_seconds

    @property
    def url(self) -> str:
        if not self._url:
            raise ValueError(
                "Attribute 'url' is empty. "
                "Make sure you set a valid URL when initializing / subclassing the 'WebPage' class. "
            )

        return self._url

    def open(self, *, maximize_window: bool = True) -> None:
        if maximize_window:
            self._driver.maximize_window()

        self._driver.get(self.url)

    def close(self) -> None:
        self._driver.quit()
