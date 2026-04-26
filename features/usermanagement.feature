Feature: User Management
  Background:
    Given the login page is opened
    And the cookie modal is closed

    Scenario: Register user
      Given the name 'Test User 1' is entered
      And the email 'testing100@testing100.com' is entered
      When the signup form is sent
      Then the account form appears
      Given the option 'title Mr' is selected
      And the field 'Password' is filled with 'foobar'
      And the field 'Day of Birth' is set to '3'
      And the field 'Month of Birth' is set to 'March'
      And the field 'Year of Birth' is set to '1986'
      And the field 'First name' is filled with 'John'
      And the field 'Last name' is filled with 'Doe'
      And the field 'Address' is filled with 'Lincoln Way 77.'
      And the field 'Country' is set to 'United States'
      And the field 'State' is filled with 'California'
      And the field 'City' is filled with 'San Fransisco'
      And the field 'Zipcode' is filled with 'CA 94122'
      And the field 'Mobile Number' is filled with '415 416 4178'
      When the account form is sent
      Then the 'account created!' message appears

  Scenario: Logout user

  Scenario: Re-register same user
      Given the name 'Test User 1' is entered
      And the email 'testing100@testing100.com' is entered
      When the signup form is sent
      Then the 'already exist' message appears
