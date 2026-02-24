from playwright.sync_api import Playwright, expect
import pytest
from playwright_automation.Lesson21.grafana_flow import GrafanaFlow

user_name = "admin"
password = "admin"
excepted_text_after_login = "Welcome to Grafana"
actual_txt_after_login = "Welcome to Grafana"


class TestGrafanaLoginPage:
    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page, grafana_flows
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://localhost:4000/login")
        #Init Page Objects:
        grafana_flows = GrafanaFlow(page)
        yield
        context.close()
        page.close()

    def test01_grafana_login_page_succsefully(self):
        grafana_flows.sign_in(user_name,password)
        assert grafana_flows.get_header() ==actual_txt_after_login