Feature: Delete User

  Background:
    Given the 'Home' page is opened
    And the cookie modal is closed
    And the user is logged out

  Scenario: Successful user deletion
    Given the user is logged in
    And the 'Home' page is opened
    When the button 'Delete Account' of 'Navbar' is clicked
    When the button 'Delete Account' of 'Navbar' is clicked
    Then the message 'permanently deleted' appears
    Given the 'Login' page is opened
    Given the text field 'Email Address' of 'Login Form' is set to 'johndoe@unitesting.com'
    And the text field 'Password' of 'Login Form' is set to 'VerySecret1'
    When the button 'Login' of 'Login Form' is clicked
    Then the message 'email or password is incorrect' appears
