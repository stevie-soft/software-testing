Feature: Cart

  Background:
    Given the 'Home' page is opened
    And the cookie modal is closed
    And the user is logged in

  Scenario Outline: Adding items to cart
    Given the 'Products' page is opened
    And the products '<product_ids>' is added to cart
    When the 'Cart' page is opened
    Then the cart displays a total amount of '<amount>' products
    Examples:
      | product_ids | amount |
      | 1,2,3 | 3 |
      | 4 | 4 |
      | 5,6 | 6 |
      | 7,8 | 8 |
      | 9,10,11 | 11 |
      | 12 | 12 |
