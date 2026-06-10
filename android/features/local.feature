Feature: BrowserStack App Automate local test
  As a BrowserStack user
  I want the local sample app to reach a service over the BrowserStack Local tunnel
  So that I can verify BrowserStack Local tunnelling works for mobile apps

  Scenario: Reach the local endpoint from the device
    Given I have launched the local sample app
    When I trigger the local network test
    Then the app reports it is up and running
