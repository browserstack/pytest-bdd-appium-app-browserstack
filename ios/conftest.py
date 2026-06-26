import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions


@pytest.fixture(scope="function")
def driver(request):
    """Appium driver fixture shared by the pytest-bdd step definitions.

    Under `browserstack-sdk pytest`, the SDK injects the app, device, and
    credentials from browserstack.yml (or the BROWSERSTACK_USERNAME /
    BROWSERSTACK_ACCESS_KEY env vars), so a bare XCUITestOptions() is enough.
    """
    options = XCUITestOptions()
    drv = webdriver.Remote("https://hub.browserstack.com/wd/hub", options=options)
    yield drv
    drv.quit()
