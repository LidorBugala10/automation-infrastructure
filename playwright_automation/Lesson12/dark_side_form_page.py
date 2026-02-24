import allure 
import pytest
from playwright.sync_api import Playwright, expect,Page
class AtidFormPage:
    def __init__(self,page:Page):
        self.page = page 
        self.first_name_field = page.locator('[id="name"]')
        self.last_name_field = page.locator('[id="lastName"]')
        self.country_selector = '[id="country"]'
        self.submit_btn = page.locator('[type="submit"]')
        self.header_message = page.locator('//h2')
        self.success_message = page.locator('[id="message-area"]')

    @allure.step("Fill Form:")
    def fill_form(self,first_name,last_name,country):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.page.select_option(self.country_selector,value=country)
        self.submit_btn.click()

    def get_header_massage(self):    
        header_massage =self.header_message.inner_text()
        print(f"\nThe header massage is :{header_massage}")
        return header_massage
    
    def get_massage(self):
        massage = self.success_message.inner_text()
        print(f"\nThe message is : {massage}")
        return massage

        
            
      

