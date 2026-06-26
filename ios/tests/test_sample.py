import os

from pytest_bdd import scenario, given, when, then, parsers
from appium.webdriver.common.appiumby import AppiumBy

FEATURES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "features")


@scenario(os.path.join(FEATURES, "sample.feature"), "Enter text and verify the output")
def test_text_button():
    """BStackSampleApp.ipa: enter text and assert the output echoes it."""


@given("I have launched the BStack sample app")
def launch_app(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text Button").click()


@when(parsers.parse('I enter the text "{text}"'))
def enter_text(driver, text):
    field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text Input")
    field.send_keys(text + "\n")


@then(parsers.parse('the output shows "{expected}"'))
def output_matches(driver, expected):
    output = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text Output").text
    assert output == expected
