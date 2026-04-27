Feature: Login User

  Background:
    Given the 'Home' page is opened 
    And the cookie modal is closed
    And the user is logged out
    And the 'Login' page is opened
    And the cookie modal is closed

  Scenario: Successful login
    Given the text field 'Email Address' of 'Login Form' is set to 'johndoe@unitesting.com'
    And the text field 'Password' of 'Login Form' is set to 'VerySecret1'
    When the button 'Login' of 'Login Form' is clicked
    Then the message 'Logged in as' appears

  Scenario: Login with invalid credentials
    Given the text field 'Email Address' of 'Login Form' is set to 'verybad@notvalid.com'
    And the text field 'Password' of 'Login Form' is set to 'doesnotmatterright?'
    When the button 'Login' of 'Login Form' is clicked
    Then the message 'email or password is incorrect' appears
