import allure
import pytest
from playwright.sync_api import Playwright, expect
from playwright_automation.Lesson15.sauce_demo_form_page import SauceDemoFormPage
from playwright_automation.Lesson15.sauce_demo_login_page import SauceDemoLoginPage
from playwright_automation.Lesson15.sauce_demo_my_cart_page import SauceDemoMyCartPage

class TestSauceDemo:
    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page, login_page,form_page,my_cart
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        login_page = SauceDemoLoginPage(page)
        form_page = SauceDemoFormPage(page)
        my_cart = SauceDemoMyCartPage(page)
        yield
        context.close()
        page.close()

    @allure.title("Test01 - Verify Button is Displayed")
    @allure.description("This test perform login,fill form and then verify button is displayed")
    def test01_verify_button_displayed(self): 
        login_page.sign_in("standard_user","secret_sauce")
        form_page.get_all_products()
        form_page.get_all_products_price()
        form_page.get_all_description()
        form_page.add_prodect()
        form_page.get_cart_with_product()
        my_cart.remove_prodect()
        assert form_page.get_cart_with_product() == 0
    
   
    
        
        

       
        
    
