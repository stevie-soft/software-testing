from core import DomElement
from sites.automationexercise.products.item_added_modal import ItemAddedModal
from sites.automationexercise.website import HomePage


class ProductsPage(HomePage):
    SUBPATH = "products"

    def add_to_cart(self, product_id: str):
        add_to_cart_button = DomElement(
            driver=self.driver,
            matcher=f'a[data-product-id="{product_id}"]',
        )
        add_to_cart_button.click()

    def dismiss_item_added_modal(self):
        modal = ItemAddedModal(self.driver)
        modal.dismiss()
