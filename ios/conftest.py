import os

import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions


@pytest.fixture(scope="function")
def driver(request):
    """Appium driver fixture shared by the pytest-bdd step definitions.

    The BrowserStack SDK injects the app + device capabilities from
    browserstack.yml, so an empty XCUITestOptions object is enough.
    """
    options = XCUITestOptions()
    options.set_capability("bstack:options", {
        "userName": os.environ.get("BROWSERSTACK_USERNAME", "YOUR_USERNAME"),
        "accessKey": os.environ.get("BROWSERSTACK_ACCESS_KEY", "YOUR_ACCESS_KEY"),
    })
    drv = webdriver.Remote("https://hub.browserstack.com/wd/hub", options=options)
    yield drv
    drv.quit()
