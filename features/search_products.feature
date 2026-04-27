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