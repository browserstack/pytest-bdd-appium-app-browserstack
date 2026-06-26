Feature: BrowserStack App Automate sample test
  As a BrowserStack user
  I want to search Wikipedia in the WikipediaSample app
  So that I can verify search results are returned

  Scenario: Search Wikipedia for BrowserStack
    Given I have launched the Wikipedia sample app
    When I search Wikipedia for "BrowserStack"
    Then search results are displayed
