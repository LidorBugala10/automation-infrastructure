import allure 
import pytest
from playwright.sync_api import Playwright, expect,Page

class SauceDemoLoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.user_name_field = page.locator("[data-test='username']")
        self.password_field =  page.locator("[data-test='password']")
        self.login_btn  = page.locator("[data-test='login-button']")
        

        
    @allure.step("Sign in :")
    def sign_in(self,user_name,password):
        self.user_name_field.fill(user_name)
        self.password_field.fill(password)
        self.login_btn.click()

    def my_card(self):
        self.my_card.click()     