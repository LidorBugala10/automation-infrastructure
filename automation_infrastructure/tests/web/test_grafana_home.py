import allure
from playwright.sync_api import Playwright, expect
import pytest
from data.web.grafana_data import *
from extensions.web_verifications import WebVerify
from workflows.web.grafana_flow import GrafanaFlow
from smart_assertions import soft_assert, verify_expectations


class TestGrafanaWeb:

    @allure.title("Create new team from Home Page")
    @allure.description("Verify that a new team can be created successfully and appears in the teams list")
    def test_create_new_team(self,home_flows:GrafanaFlow):
        home_flows.create_new_team(NAME_OF_TEAM,EMAIL)
        WebVerify.string_contained(home_flows.get_name_of_team(),EXPECTED_MESSAGE)

    @allure.title("Delete existing team from Home Page")
    @allure.description("Verify that deleting an existing team removes it from the system and displays correct confirmation message")
    def test_delete_team(self,home_flows:GrafanaFlow):
        home_flows.delete_team(NAME_OF_TEAM,EMAIL)
        WebVerify.strings_are_equal(home_flows.get_text_of_deleted_team(),TEXT_AFTER_DELETE_TEAM)  


    @allure.title("Search for existing item from Home Page")
    @allure.description("Verify that searching for a valid item navigates to the correct profiles page")
    def test_search_for_existing_item(self,home_flows:GrafanaFlow):
        home_flows.click_on_search_item(NAME_OF_ITEM)
        WebVerify.string_contained(home_flows.get_home_header_profiles(),HOME_HEADER_PROFILES)


    @allure.title("Search with invalid item name")
    @allure.description("Verify that searching with an invalid item name shows appropriate 'not found' message")
    def test_search_with_invalid_item(self,home_flows:GrafanaFlow):
        home_flows.search_item_with_invalid_name(INVALID_NAME)
        WebVerify.strings_are_equal(home_flows.get_search_massage(),SEARCH_MASSAGE)    


    @allure.title("Verify total number of menu items in Administration page")
    @allure.description("Verify that the Administration page displays the expected total number of menu items in the left navigation panel" )
    def test_count_the_menu_item(self,home_flows:GrafanaFlow):
        WebVerify.count(home_flows.grafana_administration_page.menu_items,EXPECTED_TOTAL_MENU_ITEMS)
       
    @allure.title("Delete all users except admin user")
    @allure.description("Verify that all users except the default admin user can be deleted and that the remaining number of users matches the expected result")
    def test_deleting_users(self,home_flows:GrafanaFlow):
        home_flows.navigate_to_users()
        home_flows.delete_all_users_except_admin()
        WebVerify.count(home_flows.grafana_administration_page.rows_of_users,EXPECTED_RESULT_AFTER_DELETE)

    def test_verify_google_apps(self,home_flows:GrafanaFlow):
        home_flows.google_products(APP_NAME)
        home_flows.get_all_google_app()
        soft_assert(home_flows.get_products_amount() == EXPECTED_GOOGLE_APPS_AMOUNT,
            f"Expected 8 apps but found {home_flows.get_products_amount()}")
        WebVerify.soft_contain_in_list("Google", home_flows.get_all_google_app())
        WebVerify.soft_all()

