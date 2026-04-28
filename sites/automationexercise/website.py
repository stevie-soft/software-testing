from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core import DomElement
from sites.automationexercise.home.home_page import HomePage
from sites.automationexercise.cart.cart_page import CartPage
from sites.automationexercise.common.cookie_modal import CookieModal
from sites.automationexercise.common.navbar import NavBar
from sites.automationexercise.login.login_form import LoginForm
from sites.automationexercise.login.login_page import LoginPage
from sites.automationexercise.login.signup_form import SignupForm
from sites.automationexercise.products.products_page import ProductsPage
from sites.automationexercise.products.search_products_form import SearchProductsForm
from sites.automationexercise.signup.account_form import AccountForm


class AutomationExerciseWebsite:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.pages = {
            "Home": HomePage(driver),
            "Login": LoginPage(driver),
            "Products": ProductsPage(driver),
            "Cart": CartPage(driver),
        }
        self.scopes = {
            "Navbar": NavBar(driver),
            "Account Form": AccountForm(driver),
            "Signup Form": SignupForm(driver),
            "Login Form": LoginForm(driver),
            "Search Products Form": SearchProductsForm(driver),
        }
        self.cookie_modal = CookieModal(driver)
        self.navbar = NavBar(driver)

    def says(self, text: str, timeout_seconds: float = 10.0) -> bool:
        body = DomElement(
            driver=self.driver,
            matcher="body",
            matcher_type=By.TAG_NAME,
            timeout_seconds=timeout_seconds,
        )
        return body.says(text)

    def has_cookie(self, cookie_name: str) -> bool:
        return self.driver.get_cookie(cookie_name) is not None  # type: ignore

    def count(self, selector: str) -> int:
        web_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return len(web_elements)

    def close_ads(self) -> None:
        script = """
            const selectors = `
                iframe#google_esf,
                ins[class*="adsbygoogle"]
            `;

            const elements = [...document.querySelectorAll(selectors)];
            elements.forEach(_element => _element.remove());

            if (window.location.hash === "#google_vignette") {
                history.replaceState(
                    null,
                    document.title,
                    window.location.pathname + window.location.search
                );
            }
        """
        self.driver.execute_script(script)  # type: ignore
