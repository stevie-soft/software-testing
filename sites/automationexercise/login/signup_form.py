from core import DomElement, HtmlElement


class SignupForm(HtmlElement):
    NAME_FIELD = DomElement(
        "input",
        {
            "data-qa": "signup-name",
        },
    )
    EMAIL_FIELD = DomElement(
        "input",
        {
            "data-qa": "signup-email",
        },
    )
    SIGNUP_BUTTON = DomElement(
        "button",
        {
            "data-qa": "signup-button",
        },
    )

    def enter_name(self, name: str) -> None:
        self.html.fill(self.NAME_FIELD, name)

    def enter_email(self, email: str) -> None:
        self.html.fill(self.EMAIL_FIELD, email)

    def send(self) -> None:
        self.html.click_on(self.SIGNUP_BUTTON)
