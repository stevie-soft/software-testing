from core import HtmlElement


class NavBar(HtmlElement):
    ELEMENTS = {
        "Logout": ("a", {"href": "/logout"}),
        "Delete Account": ("a", {"href": "/delete_account"}),
    }
