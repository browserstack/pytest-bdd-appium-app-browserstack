import os
import time

from pytest_bdd import scenario, given, when, then, parsers
from appium.webdriver.common.appiumby import AppiumBy

FEATURES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "features")


@scenario(os.path.join(FEATURES, "sample.feature"), "Search Wikipedia for BrowserStack")
def test_search_wikipedia():
    """WikipediaSample.apk: search Wikipedia and assert results appear."""


@given("I have launched the Wikipedia sample app")
def launch_app(driver):
    # The SDK launches the app (WikipediaSample.apk) from browserstack.yml.
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia").click()


@when(parsers.parse('I search Wikipedia for "{query}"'))
def search_wikipedia(driver, query):
    search = driver.find_element(
        AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
    search.send_keys(query)
    time.sleep(5)


@then("search results are displayed")
def results_displayed(driver):
    results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    assert len(results) > 0
