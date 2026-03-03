import pytest
import base64
from pytest import FixtureRequest
from playwright.sync_api import APIRequestContext, Playwright
from data.api.grafana_api_data import *
from data.web.grafana_data import *
from extensions.db_actions import DBActions
from extensions.ui_actions import UIActions
from utils.common_ops import load_config
from utils.fixture_helpers import get_browser
from workflows.api.grafana_api_flows import GrafanaApiFlows
from workflows.web.grafana_flow import GrafanaFlow
# from workflows.re import ReactShoppingCartFlow
# Load the configuration
CONFIG = load_config()     

@pytest.fixture(scope="class")
def page(playwright: Playwright, request:FixtureRequest):
    browser = get_browser(playwright,CONFIG["BROWSER_TYPE"].lower())
    context = browser.new_context(no_viewport=True)        
    page = context.new_page()
    UIActions.navigate_to(page,GRAFANA_URL)
    yield page    
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

@pytest.fixture
def grafana_api_flows(request_context:APIRequestContext):
    return GrafanaApiFlows(request_context)




@pytest.fixture
def home_flows(web_flow:GrafanaFlow,page):
    web_flow.sign_in(USER_NAME,PASSWORD)
    web_flow.skip_change_password()
    #     web_flow.skip_change_password()
    # if  web_flow.is_signed_in() == False:
    #     web_flow.sign_in(USER_NAME,PASSWORD)
    #     web_flow.skip_change_password()

    return GrafanaFlow(page)

@pytest.fixture
def web_flow(page):
    return GrafanaFlow(page)
    
    
    
@pytest.fixture(scope= "class")
def db(request:FixtureRequest):
    db = DBActions(CONFIG["DB_PATH"])
    yield db
    db.close_db()

