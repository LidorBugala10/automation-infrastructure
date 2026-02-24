import allure 
import pytest
from playwright.sync_api import Playwright, expect,Page

class FishTankMarketLoginPage:
    def __init__(self,page:Page):
        self.page = page
        iframe1 = page.frame_locator('//iframe')
        self.User_name_field = iframe1.locator('[type="text"]')
        self.Password_field = iframe1.locator('[id="password"]')
        self.Submit_button = iframe1.locator('[id="submitBtn"]')
        self.header_text_after_login_ = page.locator('[class="logo"]')

    @allure.step("Sign in:")
    def sign_in(self,User_name,Password):
        self.User_name_field.fill(User_name)
        self.Password_field.fill(Password)
        self.Submit_button.click() 

    @allure.step("Verify the header text after login:")    
    def header_text_after_login(self):
        self.header_text_after_login_.inner_text()

