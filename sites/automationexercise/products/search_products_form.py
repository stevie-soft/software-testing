from core import HtmlElement


class SearchProductsForm(HtmlElement):
    ELEMENTS = {
        "Search Product": ("input", {"id": "search_product"}),
        "Search": ("button", {"id": "submit_search"}),
        "Brand POLO": ("a", {"href": "/brand_products/Polo"}),
        "Brand H&M": ("a", {"href": "/brand_products/H&M"}),
        "Brand Madame": ("a", {"href": "/brand_products/Madame"}),
        "Brand Babyhug": ("a", {"href": "/brand_products/Babyhug"}),
        "Brand Kookie Kids": ("a", {"href": "/brand_products/Kookie Kids"}),
        "Brand Biba": ("a", {"href": "/brand_products/Biba"}),
    }
