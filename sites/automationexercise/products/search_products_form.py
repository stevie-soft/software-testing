from core import HtmlElement


class SearchProductsForm(HtmlElement):
    ELEMENTS = {
        "Search Product": ("input", {"id": "search_product"}),
        "Search": ("button", {"id": "submit_search"}),
        "Category Women": ("a", {"href": "#Women"}),
        "Category Men": ("a", {"href": "#Men"}),
        "Category Kids": ("a", {"href": "#Kids"}),
        "Women Saree": ("a", {"href": "/category_products/7"}),
        "Women Tops": ("a", {"href": "/category_products/2"}),
        "Men Shirts": ("a", {"href": "/category_products/3"}),
        "Men Jeans": ("a", {"href": "/category_products/6"}),
        "Kids Dress": ("a", {"href": "/category_products/4"}),
        "Kids Clothes": ("a", {"href": "/category_products/5"}),
        "Brand POLO": ("a", {"href": "/brand_products/Polo"}),
        "Brand H&M": ("a", {"href": "/brand_products/H&M"}),
        "Brand Madame": ("a", {"href": "/brand_products/Madame"}),
        "Brand Babyhug": ("a", {"href": "/brand_products/Babyhug"}),
        "Brand Kookie Kids": ("a", {"href": "/brand_products/Kookie Kids"}),
        "Brand Biba": ("a", {"href": "/brand_products/Biba"}),
    }
