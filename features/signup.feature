Feature: User Signup
  Background:
    Given the login page is opened
    And the cookie modal is closed

    Scenario: Register user
      Given the name entered is 'Test User 1'
      And the email entered is 'testing100@testing100.com'
      When the signup form is sent
      Then the account form appears