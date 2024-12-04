import pytest

from selene import browser
from selenium.webdriver import FirefoxOptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from selenium.webdriver.common.devtools.v129.target import attach_to_browser_target

from utils import attach


@pytest.fixture(scope='function')
def setup_browser_remote():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "114.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    my_browser = Browser(Config(driver=driver))

    yield my_browser

    attach.add_screenshot(my_browser)
    attach.add_logs(my_browser)
    attach.add_html(my_browser)
    attach.add_video(my_browser)


    my_browser.quit()

#
# @pytest.fixture(scope='function')
# def setup_browser_local():
#     browser.config.driver_name = 'firefox'
#     browser.config.base_url = 'https://demoqa.com'
#     browser.config.timeout = 7.0
#     options = FirefoxOptions()
#     options.add_argument("--width=1920")
#     options.add_argument("--height=1080")
#     options.timeouts = {'pageLoad': 3000}
#     options.page_load_strategy = 'none'
#     browser.config.driver_options = options
#
#     yield
#
#     browser.quit()