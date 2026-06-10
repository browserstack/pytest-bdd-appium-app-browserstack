import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def driver(request):
    """Appium driver fixture shared by the pytest-bdd step definitions.

    The BrowserStack SDK injects the app + device capabilities from
    browserstack.yml, so an empty UiAutomator2Options object is enough — no
    hub URL caps or device caps are set here. When launched with
    `browserstack-sdk pytest`, the session is routed to the BrowserStack
    cloud automatically.
    """
    options = UiAutomator2Options()
    options.set_capability("bstack:options", {
        "userName": os.environ.get("BROWSERSTACK_USERNAME", "YOUR_USERNAME"),
        "accessKey": os.environ.get("BROWSERSTACK_ACCESS_KEY", "YOUR_ACCESS_KEY"),
    })
    drv = webdriver.Remote("https://hub.browserstack.com/wd/hub", options=options)
    yield drv
    drv.quit()
