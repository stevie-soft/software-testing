from core import HtmlElement


class CookieModal(HtmlElement):
    ELEMENTS = {"Consent": ("button", {"aria-label": "Beleegyezés"})}

    def accept(self) -> None:
        self.elements["Consent"].click()

    def is_visible(self) -> bool:
        return self.elements["Consent"].is_visible()
