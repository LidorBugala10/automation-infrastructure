import allure
import pytest
from playwright.sync_api import Playwright, expect
from playwright_automation.Lesson16.fish_tank_market_form_page import FishTankMarketFormPage
from playwright_automation.Lesson16.fish_tank_market_login_page import FishTankMarketLoginPage

user_name = "fish_matter"
password = "feed_fish"
all_products_prices = "6"
all_product_names = "6"
header_text_after_login = "Fresh Catch"

class TestFishTankMarket:
    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page, login_page,form_page
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/fish-tank-market/")
        login_page = FishTankMarketLoginPage(page)
        form_page = FishTankMarketFormPage(page)
        login_page.sign_in(user_name,password)

        yield
        context.close()
        page.close()

    @allure.title("Test01 - Verify login,fill form ,get all names of products and their price")
    @allure.description("This test perform login successfully")
    def test_verify_login(self):
        login_page.header_text_after_login()
        assert header_text_after_login == header_text_after_login
      
     
    @allure.title("Test02 - Verify fill form and get all names of products and their prices")
    @allure.description("This test perform fill form,get all names of products and their prices")
    def test_verify_all_product_names(self):
        form_page.get_all_product_names()
        print("=============================================")
        form_page.get_all_products_prices()
        form_page.get_all_products_prices_and_names()
        assert all_product_names == all_products_prices
        
        
      
