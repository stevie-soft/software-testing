Feature: Register User

  Background:
    Given the user is logged out
    And the 'Login' page is opened
    And the cookie modal is closed

  Scenario: Successful registration
    Given the text field 'Name' of 'Signup Form' is set to 'Test User'
    And the text field 'Email' of 'Signup Form' is set to 'testing100@unitesting.com'
    When the button 'Signup' of 'Signup Form' is clicked
    Then the message 'Enter account information' appears
    Given the radio button 'Mr.' of 'Account Form' is selected
    And the text field 'Password' of 'Account Form' is set to 'Super$ecret1'
    And the select field 'Day of Birth' of 'Account Form' is set to '3'
    And the select field 'Month of Birth' of 'Account Form' is set to 'March'
    And the select field 'Year of Birth' of 'Account Form' is set to '1986'
    And the text field 'First name' of 'Account Form' is set to 'Test'
    And the text field 'Last name' of 'Account Form' is set to 'User'
    And the text field 'Address' of 'Account Form' is set to 'Lincoln Way 77.'
    And the select field 'Country' of 'Account Form' is set to 'United States'
    And the text field 'State' of 'Account Form' is set to 'California'
    And the text field 'City' of 'Account Form' is set to 'San Fransisco'
    And the text field 'Zipcode' of 'Account Form' is set to 'CA 94122'
    And the text field 'Mobile Number' of 'Account Form' is set to '415 416 4178'
    When the button 'Create Account' of 'Account Form' is clicked
    Then the message 'account created!' appears
    When the button 'Continue' of 'Account Form' is clicked
    Then the message 'Logged in as' appears

  Scenario: Registration fails when email is already in use
    Given the text field 'Name' of 'Signup Form' is set to 'John Doe'
    And the text field 'Email' of 'Signup Form' is set to 'johndoe@unitesting.com'
    When the button 'Signup' of 'Signup Form' is clicked
    Then the message 'already exist' appears