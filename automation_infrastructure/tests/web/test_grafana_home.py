from playwright.sync_api import Playwright, expect
import pytest
from data.web.grafana_data import *
from extensions.web_verifications import WebVerify
from workflows.web.grafana_flow import GrafanaFlow


class TestGrafanaWeb:

    def test01_home_page(self,home_flows:GrafanaFlow):
        home_flows.create_new_team(NAME_OF_TEAM,EMAIL)
        WebVerify.string_contained(home_flows.get_name_of_team(),EXPECTED_MESSAGE)

    # def test02_home_page(self,home_flows:GrafanaFlow):
    #     home_flows.delete_team(NAME_OF_TEAM,EMAIL)
    #     WebVerify.strings_are_equal(home_flows.get_text_of_deleted_team(),TEXT_AFTER_DELETE_TEAM)  

    # def test03_home_page(self,home_flows:GrafanaFlow):
    #     home_flows.click_on_search_item(NAME_OF_ITEM)
    #     WebVerify.string_contained(home_flows.get_home_header_profiles(),HOME_HEADER_PROFILES)

    # def test04_home_page(self,home_flows:GrafanaFlow):
    #     home_flows.search_item_with_invalid_name(INVALID_NAME)
    #     WebVerify.strings_are_equal(home_flows.get_search_massage(),SEARCH_MASSAGE)    


    def test05_count_the_menu_item(self,home_flows:GrafanaFlow):
        WebVerify.count(home_flows.grafana_administration_page.menu_items,EXPECTED_TOTAL_MENU_ITEMS)
       
    def test06_deleting_users(self,home_flows:GrafanaFlow):
        home_flows.navigate_to_users()
        home_flows.delete_all_users_except_admin()
        WebVerify.count(home_flows.grafana_administration_page.rows_of_users,EXPECTED_RESULT_AFTER_DELETE)

