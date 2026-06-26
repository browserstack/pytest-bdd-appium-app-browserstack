Feature: BrowserStack App Automate sample test
  As a BrowserStack user
  I want to enter text in the BStack sample app
  So that I can verify the text output echoes my input

  Scenario: Enter text and verify the output
    Given I have launched the BStack sample app
    When I enter the text "hello@browserstack.com"
    Then the output shows "hello@browserstack.com"
