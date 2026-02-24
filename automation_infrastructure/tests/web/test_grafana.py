from playwright.sync_api import Playwright, expect
import pytest
from automation_infrastructure.extensions.web_verifications import WebVerify
from automation_infrastructure.workflows.web.grafana_flow import GrafanaFlow
from automation_infrastructure.data.web.grafana_data import *


class TestGrafanaLoginPage:
    def test_verify_(self,web_flow:GrafanaFlow):
        web_flow.sign_in(USER_NAME,PASSWORD)
        web_flow.skip_password_change()
        WebVerify.text(web_flow.grafana_login_page)