from typing import cast

from behave import step  # type: ignore | Incomplete typing | **kwargs: Unknown
from behave.runner import Context
from features.context import AutomationExerciseContext
from sites.automationexercise.website import ProductsPage


@step("'{count_str}' products appear")
def count_products(context: Context, count_str: str):
    context = cast(AutomationExerciseContext, context)
    expected_count = int(count_str)
    assert expected_count == context.site.count(".single-products")


@step("the products '{product_ids}' is added to cart")
def add_to_cart(context: Context, product_ids: str):
    context = cast(AutomationExerciseContext, context)
    page = ProductsPage(context.site.driver)

    for product_id in product_ids.split(","):
        page.add_to_cart(product_id.strip())
        page.dismiss_item_added_modal()


@step("the cart displays a total amount of '{amount_str}' products")
def check_cart_money(context: Context, amount_str: str):
    context = cast(AutomationExerciseContext, context)
    amount = int(amount_str)
    count = context.site.count(".cart_product")
    print(f"CART SIZE: {count}")
    assert amount == count
