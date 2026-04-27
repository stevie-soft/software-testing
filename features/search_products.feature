Feature: Search products

  Background:
    Given the 'Home' page is opened
    And the cookie modal is closed
    And the user is logged in
    
  Scenario Outline: Find products
    Given the 'Products' page is opened
    And the text field 'Search Product' of 'Search Products Form' is set to '<keyword>'
    When the button 'Search' of 'Search Products Form' is clicked
    Then '<matches>' products appear
    Examples:
      | keyword | matches |
      | blue | 7 |
      | red | 3 |
      | black | 0 |
      | white | 3 |
      | green | 3 |
      | purple | 0 |

  Scenario Outline: Filter brands
    Given the 'Products' page is opened
    When the button 'Brand <brand>' of 'Search Products Form' is clicked
    Then '<products>' products appear
    Examples:
      | brand | products | 
      | POLO | 6 |
      | H&M | 5 |
      | Madame | 5 |
      | Babyhug | 4 |
      | Kookie Kids | 3 |
      | Biba | 5 |

  Scenario Outline: Toggle categories
    Given the 'Products' page is opened
    When the button 'Category <category>' of 'Search Products Form' is clicked
    Then the element '<subcategory>' of 'Search Products Form' becomes clickable
    Examples:
      | category | subcategory |
      | Women | Women Saree |
      | Women | Women Tops |
      | Men | Men Shirts |
      | Men | Men Jeans |
      | Kids | Kids Dress |
      | Kids | Kids Clothes |