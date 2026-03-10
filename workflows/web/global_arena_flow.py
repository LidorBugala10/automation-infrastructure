import allure
from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from extensions.ui_actions import UIActions
from page_objects.web.global_arena_cart_page import GlobalArenaCartPage
from page_objects.web.global_arena_home_page import GlobalArenaHomePage
from page_objects.web.global_arena_login_page import GlobalArenaLoginPage
class GlobalArenaFlow:
    def __init__(self,page:Page):
        self.page = page
        self.global_arena_login_page = GlobalArenaLoginPage(page)
        self.global_arena_home_page = GlobalArenaHomePage(page)
        self.global_arena_cart_page = GlobalArenaCartPage(page)


    @allure.step("Buy ticket and complete checkout")
    def buy_ticket_and_checkout(self,user_name,password,first_name,last_name,email,phone_number,street_address,city,zip_code,card_number,expiry_date,cvv):
        UIActions.click(self.global_arena_login_page.login_link)
        UIActions.update_text(self.global_arena_login_page.login_user_name_input,user_name)
        UIActions.update_text(self.global_arena_login_page.login_password_input,password)
        UIActions.click(self.global_arena_login_page.login_submit_button )
        UIActions.click(self.global_arena_home_page.browse_all_tickets_button)
        UIActions.click(self.global_arena_home_page.add_additional_ticket_button)
        UIActions.click(self.global_arena_home_page.add_another_ticket_button)
        UIActions.click(self.global_arena_home_page.add_ticket_button)
        UIActions.click(self.global_arena_home_page.cart_item)
        UIActions.click(self.global_arena_cart_page.proceed_to_checkout)
        UIActions.update_text(self.global_arena_cart_page.first_name_field,first_name)
        UIActions.update_text(self.global_arena_cart_page.last_name_field,last_name)
        UIActions.update_text(self.global_arena_cart_page.email_address_field,email)
        UIActions.update_text(self.global_arena_cart_page.phone_number_field,phone_number)
        UIActions.update_text(self.global_arena_cart_page.street_address_field,street_address)
        UIActions.update_text(self.global_arena_cart_page.city_field,city)
        UIActions.update_text(self.global_arena_cart_page.zip_code_field,zip_code)
        UIActions.update_text(self.global_arena_cart_page.card_number_field,card_number)
        UIActions.update_text(self.global_arena_cart_page.expiry_date_field,expiry_date)
        UIActions.update_text(self.global_arena_cart_page.cvv_field,cvv)
        UIActions.click(self.global_arena_cart_page.check_box_button)
        UIActions.click(self.global_arena_cart_page.complete_purchase) 
        UIActions.scroll_down(self.page, 600)



    @allure.step("Login to Global Arena")
    def login_success(self,user_name,password):
        UIActions.click(self.global_arena_login_page.login_link)
        UIActions.update_text(self.global_arena_login_page.login_user_name_input,user_name)
        UIActions.update_text(self.global_arena_login_page.login_password_input,password)
        UIActions.click(self.global_arena_login_page.login_submit_button )

    @allure.step("Get home page header title")    
    def get_home_page_header_title(self) -> str:
        home_page_header = UIActions.get_text(self.global_arena_home_page.home_page_title)
        print(f"\nHome page Header title is : {home_page_header}")
        return home_page_header  
    
    
    @allure.step("Logout from Global Arena")
    def logout_success(self,user_name,password):
        UIActions.click(self.global_arena_login_page.logout_link)
        UIActions.click(self.global_arena_login_page.login_link)
        UIActions.update_text(self.global_arena_login_page.login_user_name_input,user_name)
        UIActions.update_text(self.global_arena_login_page.login_password_input,password)
        UIActions.click(self.global_arena_login_page.login_submit_button )
     
    @allure.step("Retrieve 'My Order' element from Home Page")
    def get_my_order_message(self):
         return self.global_arena_home_page.my_order


    @allure.step("Create new user account")
    def create_new_user(self,user_name,password):
        UIActions.click(self.global_arena_login_page.logout_link)
        UIActions.click(self.global_arena_login_page.login_link)
        UIActions.click(self.global_arena_login_page.register_toggle_button )
        UIActions.update_text(self.global_arena_login_page.register_user_name_input,user_name)
        UIActions.update_text(self.global_arena_login_page.register_password_input,password)
        UIActions.click(self.global_arena_login_page.login_submit_button) 


    @allure.step("Get Home Page Header Title")
    def get_home_page_header_title(self) -> str:
        home_page_header = UIActions.get_text(self.global_arena_home_page.home_page_title)
        print(f"\nHome page Header title is : {home_page_header}")
        return home_page_header      
    
    @allure.step("Add ticket to cart")
    def add_ticket_to_cart(self):
        UIActions.click(self.global_arena_home_page.logo_item)
        UIActions.click(self.global_arena_home_page.browse_all_tickets_button)
        UIActions.click(self.global_arena_home_page.add_ticket_button)
        UIActions.click(self.global_arena_home_page.cart_item)

    @allure.step("Get event name from cart")    
    def get_event_name_from_cart(self):
        name_of_event = UIActions.get_text(self.global_arena_cart_page.evnet_message)
        print(F"\nThe name of event is :{name_of_event}")
        return name_of_event    
    
    @allure.step("Navigate back to home page")
    def navigate_back_to_home_page(self):
        UIActions.click(self.global_arena_cart_page.back_to_home_button)

    @allure.step("Verify Home page is displayed")
    def get_home_page_identifier(self):
        my_order_message_after_home = UIActions.get_text(self.global_arena_cart_page.home_page_identifier)
        print(f"\nThe message after return is :{my_order_message_after_home }")
        return my_order_message_after_home     


    @allure.step("Remove ticket from cart")
    def remove_tickets_from_cart(self):
        UIActions.click(self.global_arena_home_page.browse_all_tickets_button)
        UIActions.click(self.global_arena_home_page.add_additional_ticket_button)
        UIActions.click(self.global_arena_home_page.add_another_ticket_button)
        UIActions.click(self.global_arena_home_page.add_ticket_button)
        UIActions.click(self.global_arena_home_page.cart_item)
        UIActions.click(self.global_arena_home_page.remove_first_match_ticket_button)
        UIActions.click(self.global_arena_home_page.remove_second_match_ticket_button)
        UIActions.click(self.global_arena_home_page.remove_third_match_ticket_button)
        UIActions.click(self.global_arena_home_page.cart_item)
     
    
    @allure.step("Get cart deletion confirmation message")
    def get_cart_deletion_message(self):
        delete_cart_message = UIActions.get_text(self.global_arena_home_page.empty_cart_message)
        print(f"\nThe message after delete cart is :{delete_cart_message}")
        return delete_cart_message
  

    def all_name_of_tickets(self):  
        UIActions.click(self.global_arena_home_page.browse_all_tickets_button)
        tickets = self.global_arena_home_page.name_of_all_tickets.all()
        prices = self.global_arena_home_page.all_tickets_from_home_page.all()
        # משתמש ב-set כדי למנוע כפילויות
        unique_tickets = set()
        for i in range(len(tickets)):
            ticket_info = f"\nTicket name : {tickets[i].inner_text()} \nTicket price : {prices[i].inner_text()}"
            unique_tickets.add(ticket_info)
        for t in unique_tickets:
            print(t)
        print(f"\nTotal unique tickets: {len(unique_tickets)}")
    

    def get_all_tickes_massage(self):
        all_tickets_message = UIActions.get_text(self.global_arena_home_page.all_tickets_text)
        print(f"\nThe header message of all tickets is :{all_tickets_message}")
        return all_tickets_message


            
