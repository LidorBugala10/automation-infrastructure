import os
import time
from urllib import request
import uuid
import pytest
import base64
from pytest import FixtureRequest
from playwright.sync_api import APIRequestContext, Playwright
from data.api.grafana_api_data import *
from data.web.global_arena_data import GLOBAL_ARENA_URL
from data.web.grafana_data import *
from extensions.db_actions import DBActions
from extensions.ui_actions import UIActions
from utils.common_ops import load_config
from utils.fixture_helpers import attach_screenshot, attach_trace, get_browser
from workflows.api.grafana_api_flows import GrafanaApiFlows
from workflows.mobile.mobile_flow import Mobile_flow
from workflows.web.global_arena_flow import GlobalArenaFlow
from workflows.web.grafana_flow import GrafanaFlow
from appium import webdriver
# from workflows.re import ReactShoppingCartFlow
# Load the configuration
CONFIG = load_config()     


@pytest.fixture(scope="class")
def second_site_page(playwright: Playwright,request:FixtureRequest):
    browser = get_browser(playwright, CONFIG["BROWSER_TYPE"].lower())
    context = browser.new_context(no_viewport=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    UIActions.navigate_to(page,GLOBAL_ARENA_URL)
    page.on("console", handle_console_message)
    yield page   
    test_name = request.node.name
    trace_filename = f"./{CONFIG['TRACES_DIR']}/trace_{test_name}.zip"
    context.tracing.stop(path=trace_filename) # Stop tracing and save the trace to a file.
    # Best practice: Close page before context 
    # Best practice: Close page before context
    page.close()
    context.close()
    browser.close()



@pytest.fixture(scope="class")
def page(playwright: Playwright, request:FixtureRequest):
    browser = get_browser(playwright,CONFIG["BROWSER_TYPE"].lower())
    context = browser.new_context(no_viewport=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True) # Start tracing for this context.          
    page = context.new_page()
    UIActions.navigate_to(page,GRAFANA_URL)
    page.on("console", handle_console_message)
    yield page   
    test_name = request.node.name
    # trace_filename = f"./{CONFIG["TRACES_DIR"]}/trace_{test_name}.zip"
    # context.tracing.stop(path=trace_filename) # Stop tracing and save the trace to a file.
    # Best practice: Close page before context 
    # Best practice: Close page before context
    page.close()
    context.close()
    browser.close()

@pytest.fixture(scope="class")
def request_context(playwright: Playwright, request: FixtureRequest):
    credentials = "admin:admin"
    encoded = base64.b64encode(credentials.encode()).decode()
    request_context = playwright.request.new_context(
        base_url=GRAFANA_API_BASE_URL,
        extra_http_headers={
              "Authorization": f"Basic {encoded}",
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                }
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="class")
def mobile_setup(request:FixtureRequest):
    dc = {}
    dc['udid'] = '8dad0f967d78'
    dc['appPackage'] = 'com.atidcollege.todolist'
    dc['appActivity'] = '.MainActivity'
    dc['platformName'] = 'android'
    driver = webdriver.Remote('http://localhost:4723/wd/hub',dc)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def mobile_flow(mobile_setup):
    return Mobile_flow(mobile_setup)
    


@pytest.fixture
def grafana_api_flows(request_context:APIRequestContext):
    return GrafanaApiFlows(request_context)

@pytest.fixture
def home_flows(web_flow:GrafanaFlow,page):
    if  web_flow.is_signed_in() == False:
        web_flow.sign_in(USER_NAME,PASSWORD)
        web_flow.skip_change_password()
    return GrafanaFlow(page)



@pytest.fixture
def web_flow(page):
    return GrafanaFlow(page)

@pytest.fixture
def web_flow_ai(second_site_page):
    return GlobalArenaFlow(second_site_page)

    

@pytest.fixture(scope= "class")
def db(request:FixtureRequest):
    db = DBActions(CONFIG["DB_PATH"])
    yield db
    db.close_db()


def handle_console_message(msg):
    if msg.type == "error":
        print(f"Error detected in console: {msg.text}")
    if "the server responded with a status of 404" in msg.text:
        raise AssertionError(f"Test Failed: 404 Error Detected in Console - {msg.text}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to attach screenshots, videos, and traces to Allure reports on test failure,
    and log test case names for reporting.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Attachments (only if the test failed)
        if report.failed:
            page = item.funcargs.get("page")

            if page:
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                unique_id = str(uuid.uuid4())[:8]
                base_filename = f"{item.name}_{timestamp}_{unique_id}"

                # Attach screenshot
                screenshot_name = f"{CONFIG['SCREENSHOT_PREFIX']}_{base_filename}.png"
                screenshot_path = os.path.join(CONFIG['ALLURE_RESULTS_DIR'], screenshot_name)
                attach_screenshot(page, item.name, screenshot_path)
                # Attach trace
                trace_name = f"{CONFIG['TRACE_PREFIX']}_{item.name}_{timestamp}.zip"
                trace_path = os.path.join(CONFIG['ALLURE_RESULTS_DIR'], trace_name)
                attach_trace(page, item.name, trace_path)    

