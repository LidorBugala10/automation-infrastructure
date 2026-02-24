import allure
import pytest
from playwright.sync_api import Playwright, expect

keyword = "user_name,Password,expected_status"
data = [("standard_user","secret_sauce","valid"),
        ("standard_user","saed","invalid")]
        



class TestDdtSauceDemo:

    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page, login_page,form_page
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        yield
        context.close()
        page.close()

    @pytest.mark.parametrize(keyword,data)
    def test_ddt_sauce_demo(self,user_name,Password,expected_status):
        page.goto("https://www.saucedemo.com/")
        page.locator('[data-test="username"]').fill(user_name)
        page.locator('[data-test="password"]').fill(Password)
        page.locator('[data-test="login-button"]').click()
        if expected_status == "valid":
            actual_header = page.locator('[class="title"]').inner_text()
            print(F"\nThe actual header is :{actual_header}")
            assert actual_header == "Products"
        else :
            assert page.locator('[data-test="error"]').is_visible()

        

        
        
        


