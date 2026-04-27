Feature: Navbar

  Background:
    Given the 'Home' page is opened
    And the cookie modal is closed
    And the user is logged in

  Scenario Outline: Navigation is functioning
    When the button '<navlink>' of 'Navbar' is clicked
    Then the message '<indicator>' appears
    Examples:
      | navlink | indicator |
      | Home | practice website |
      | Products | All Products |
      | Cart | Shopping Cart |
      | Test Cases | list of test Cases | 
      | API Testing | APIs List for practice |
      | Contact us | Get In Touch |
    