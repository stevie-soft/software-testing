Feature: Logout User

  Background:
    Given the 'Home' page is opened
    And the cookie modal is closed
    And the user is logged out

  Scenario: Successful logout
    Given the user is logged in
    And the 'Home' page is opened
    When the button 'Logout' of 'Navbar' is clicked
    Given the 'Login' page is opened
    Then the message 'Login to your account' appears
