Feature: User Signup
  Background:
    Given the home page is opened

    Scenario Outline: First test
      Given the name field is filled with '<name>'
      And the 'email' field is filled with '<email>'
      Then the browser quits
      Examples:
        | name | email
        | Test User | testing100@testing100.com