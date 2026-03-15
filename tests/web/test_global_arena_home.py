import allure
from playwright.sync_api import Playwright, expect
import pytest
from data.web.global_arena_data import *
from extensions.web_verifications import WebVerify
from workflows.web.global_arena_flow import GlobalArenaFlow


class TestGlobalArenaHome:
    def test_verify_all_tickets(self,web_flow_ai:GlobalArenaFlow):
        web_flow_ai.name_and_price_of_all_tickets()
        WebVerify.strings_are_equal(web_flow_ai.get_all_tickes_massage(),EXPECTED_ALL_TICKETS_TEXT)
    

   

  