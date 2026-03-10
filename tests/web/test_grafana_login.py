import allure
from playwright.sync_api import Playwright, expect
import pytest
from data.web.grafana_data import *
from extensions.db_actions import DBActions
from extensions.web_verifications import WebVerify
from workflows.web.grafana_flow import GrafanaFlow


class TestGrafanaLoginPage:
    @allure.title("Verify login fails with invalid username and password ")
    @allure.description( "Verify that when entering invalid username and password,an appropriate error message is displayed on the login page.")
    def test_verify_incorrect_login(self,web_flow:GrafanaFlow):
        web_flow.sign_in(USER_NAME_INVALID,PASSWORD_INVALID)
        WebVerify.string_contained(web_flow.get_error_massage(),EXPECTED_ERORR_MESSAGE)

    @allure.title("Verify user can logout successfully")
    @allure.description("Verify that after successful login, the user can log out ,and is redirected back to the login page.")
    def test_verify_log_out(self,web_flow:GrafanaFlow):
        web_flow.sign_in(USER_NAME,PASSWORD)
        web_flow.skip_change_password()
        web_flow.log_out_form_garfana()
        WebVerify.strings_are_equal(web_flow.grafana_login_page.login_page_header.inner_text(),EXPECTED_HEADER)
              
    @allure.title("Verify successful login using DB and AI")
    @allure.description("Verify that login succeeds when user name and password are retrieved from the database and ai ,that the home page header is displayed")
    def test_verify_login_successfully_with_db_and_ai(self,web_flow:GrafanaFlow,db:DBActions):
        admin_user = db.get_admin_user()
        web_flow.sign_in(admin_user["user_name"],admin_user["password"])
        web_flow.skip_change_password()     
        result =  web_flow.verify_with_vision(EXPECTED_HOME_HEADER)
        WebVerify.strings_are_equal_bool(result, EXPECTED_HOME_HEADER)
        