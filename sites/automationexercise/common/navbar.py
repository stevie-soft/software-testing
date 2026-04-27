from core import HtmlElement


class NavBar(HtmlElement):
    ELEMENTS = {
        "Home": ("a", {"href": "/"}),
        "Products": ("a", {"href": "/products"}),
        "Cart": ("a", {"href": "/view_cart"}),
        "Test Cases": ("a", {"href": "/test_cases"}),
        "API Testing": ("a", {"href": "/api_list"}),
        "Contact us": ("a", {"href": "/contact_us"}),
        "Logout": ("a", {"href": "/logout"}),
        "Delete Account": ("a", {"href": "/delete_account"}),
    }
