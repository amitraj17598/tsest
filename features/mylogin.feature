Feature: Login functionality

  @sanity
  Scenario: Successful Login with Valid Credentials
    Given User launches Chrome browser
    When User opens the URL "https://jugno.racketail.com/"
    And User enters email as "admin@nexustechinnov.com" and password as "Admin95@#"
    And User clicks on Login
    Then Page title should be "Dashboard"

    When User clicks on Log out link
    Then Page title should be "Login"

    And User closes the browser
