from core import HtmlElement


class ItemAddedModal(HtmlElement):
    ELEMENTS = {
        "Continue Shopping": ("button", {"data-dismiss": "modal"}),
        "View Cart": ("a", {"href": "/view_cart"}),
    }

    def dismiss(self):
        self.elements["Continue Shopping"].click()
