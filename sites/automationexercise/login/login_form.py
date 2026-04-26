from core import HtmlElement


class LoginForm(HtmlElement):
    ELEMENTS = {
        "Email Address": ("input", {"data-qa": "login-email"}),
        "Password": ("input", {"data-qa": "login-password"}),
        "Login": ("button", {"data-qa": "login-button"}),
    }
