import allure
from playwright.sync_api import Playwright, expect
import pytest
from data.web.global_arena_data import *
from extensions.web_verifications import WebVerify
from workflows.web.global_arena_flow import GlobalArenaFlow

class TestGlobalArenaCart:

  
    @allure.title("Verify ticket purchase and checkout")
    @allure.description("This test verifies that a user can buy a ticket and complete the checkout process successfully, and the purchase confirmation message is displayed.")
    def test_verify_buy_ticket(self,web_flow_ai:GlobalArenaFlow):
        web_flow_ai.buy_ticket_and_checkout(USER_NAME,PASSWORD,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,STREET_ADDRESS,CITY,ZIP_CODE,CARD_NUMBER,EXPIRY_DATE,CVV)
        web_flow_ai.navigate_back_to_home_page()
        WebVerify.strings_are_equal(web_flow_ai.get_home_page_identifier(),EXPECTED_HOME_PAGE_HEADER_TITLE)  

    @allure.title("Verify deleting tickets from cart")
    @allure.description("This test verifies that all tickets can be removed from the cart successfully and the correct cart deletion message is displayed.")        
    def test_verify_delete_cards(self,web_flow_ai:GlobalArenaFlow):
        web_flow_ai.remove_tickets_from_cart()
        WebVerify.strings_are_equal(web_flow_ai.get_cart_deletion_message(),EXPECTED_EMPTY_CART_TEXT)   

    @allure.title("Verify adding ticket to cart")
    @allure.description("This test verifies that a ticket can be added to the cart successfully and the correct event name is displayed in the cart.")
    def test_verify_add_card_to_cart(self,web_flow_ai:GlobalArenaFlow):
        web_flow_ai.add_ticket_to_cart()
        WebVerify.strings_are_equal(web_flow_ai.get_event_name_from_cart(),EXPECTED_NAME_EVENT)    

        
 


  