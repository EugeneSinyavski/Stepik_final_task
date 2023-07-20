import allure
import datetime
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action="store", default="en",
                     help="Choose language: en/ru/es")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    def finalizer():
        if request.node.result != "passed":
            attach_screenshot(browser, request)
        browser.quit()

    request.addfinalizer(finalizer)

    browser.log_level = logging.DEBUG
    browser.test_name = request.node.name

    browser.maximize_window()

    return browser


@allure.step("Attaching screenshot for test failure")
def attach_screenshot(browser, request):
    screenshot_name = f"[{request.node.name}]:{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    allure.attach(
        body=browser.get_screenshot_as_png(),
        name=screenshot_name,
        attachment_type=allure.attachment_type.PNG
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.result = result.outcome
