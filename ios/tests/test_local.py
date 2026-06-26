import os

from pytest_bdd import scenario, given, when, then
from appium.webdriver.common.appiumby import AppiumBy

FEATURES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "features")


@scenario(os.path.join(FEATURES, "local.feature"), "Reach the local endpoint from the device")
def test_local():
    """LocalSample.ipa over the BrowserStack Local tunnel (browserstackLocal: true)."""


@given("I have launched the local sample app")
def launch_local_app(driver):
    pass


@when("I trigger the local network test")
def trigger_local_test(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "TestBrowserStackLocal").click()


@then("the app reports it is up and running")
def app_up_and_running(driver):
    result = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID, "ResultBrowserStackLocal").text
    assert "up and running" in (result or "").lower()
