import allure 
import pytest
from playwright.sync_api import Playwright, expect,Page

class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.user_name_field = page.locator("[id='username']")
        self.password_field =  page.locator("[id='password']")
        self.submit_btn  = page.locator("[type='submit']")
        
    @allure.step("Sign in :")
    def sign_in(self,user_name,password):
        self.user_name_field.fill(user_name)
        self.password_field.fill(password)
        self.submit_btn.click()