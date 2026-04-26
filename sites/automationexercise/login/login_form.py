from core import DomElement, HtmlElement


class LoginForm(HtmlElement):
    EMAIL_FIELD = DomElement(
        "input",
        {
            "data-qa": "login-email",
        },
    )
    PASSWORD_FIELD = DomElement(
        "input",
        {
            "data-qa": "login-password",
        },
    )
    LOGIN_BUTTON = DomElement(
        "button",
        {
            "data-qa": "login-button",
        },
    )
