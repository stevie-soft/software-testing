from core import HtmlElement


class SearchProductsForm(HtmlElement):
    ELEMENTS = {
        "Search Product": ("input", {"id": "search_product"}),
        "Search": ("button", {"id": "submit_search"}),
    }
