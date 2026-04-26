from core import DomElement, HtmlElement


class CookieModal(HtmlElement):
    ACCEPT_BUTTON = DomElement(
        "button",
        {
            "aria-label": "Beleegyezés",
        },
    )

    def accept(self) -> None:
        self.html.click_on(self.ACCEPT_BUTTON)

    @property
    def is_accepted(self) -> bool:
        return self.html.has_cookie("__gads")
