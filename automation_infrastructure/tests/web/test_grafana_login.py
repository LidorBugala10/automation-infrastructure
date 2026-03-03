from playwright.sync_api import Playwright, expect
import pytest
from data.web.grafana_data import *
from extensions.db_actions import DBActions
from extensions.web_verifications import WebVerify
from workflows.web.grafana_flow import GrafanaFlow


class TestGrafanaLoginPage:

    def test01_verify_incorrect_login(self,web_flow:GrafanaFlow):
        web_flow.sign_in(USER_NAME_INVALID,PASSWORD_INVALID)
        WebVerify.string_contained(web_flow.get_error_massage(),EXPECTED_ERORR_MESSAGE)



    def test02_verify_log_out(self,web_flow:GrafanaFlow):
        web_flow.sign_in(USER_NAME,PASSWORD)
        web_flow.skip_change_password()
        web_flow.log_out_form_garfana()
        WebVerify.strings_are_equal(web_flow.grafana_login_page.login_page_header.inner_text(),EXPECTED_HEADER)
              
    
    def test03_verify_login_successfully_with_db(self,web_flow:GrafanaFlow,db:DBActions):
        admin_user = db.get_admin_user()
        web_flow.sign_in(admin_user["user_name"],admin_user["password"])
        web_flow.skip_change_password()
        WebVerify.strings_are_equal(web_flow.get_home_header(),EXPECTED_HOME_HEADER)