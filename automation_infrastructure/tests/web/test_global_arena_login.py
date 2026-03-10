import allure
from playwright.sync_api import Playwright, expect
import pytest
from data.web.global_arena_data import *
from extensions.web_verifications import WebVerify
from workflows.web.global_arena_flow import GlobalArenaFlow


class TestGlobalArenaLoginPage:
    @allure.title("Verify successful login")
    @allure.description("This test verifies that a user can log in successfully and the Home Page header is displayed correctly.")
    def test_verify_login(self,web_flow_ai:GlobalArenaFlow):
        web_flow_ai.login_success(USER_NAME,PASSWORD)
        WebVerify.strings_are_equal(web_flow_ai.get_home_page_header_title(),EXPECTED_HOME_HEADER)

    @allure.title("Verify logout functionality")
    @allure.description("This test verifies that a user can log out successfully and the 'My Order' message or identifier is visible on the Home Page.")
    def test_logout(self,web_flow_ai:GlobalArenaFlow):
        web_flow_ai.logout_success(USER_NAME,PASSWORD)
        WebVerify.visible(web_flow_ai.get_my_order_message())     

                      
    @allure.title("Verify user creation")
    @allure.description("This test verifies that a new user can be created successfully and after creation the Home Page header is displayed as expected.") 
    def test_verify_create_user(self,web_flow_ai:GlobalArenaFlow): 
        web_flow_ai.create_new_user(REGISTERED_UESR_NAME,REGISTERED_PASSWORD)
        WebVerify.strings_are_equal(web_flow_ai.get_home_page_header_title(),EXPECTED_HOME_HEADER)


   




