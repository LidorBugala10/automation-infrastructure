import allure 
import pytest
from playwright.sync_api import Playwright, expect
from playwright_automation.Lesson11.test_atid_login_page import AtidLoginPage
first_name = "lidor"
last_name = "bugala"
destination = "beach"


class TestAtidPage:

    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page, login_page
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/practice-form.html") 
        login_page = AtidLoginPage(page)
        yield
        context.close()
        page.close()

    @allure.title("Test01- veridy button is displayed")
    @allure.description("This test perform login")  
    def test01_verify_button_displayed(self):
        login_page.sign_in(first_name,last_name,destination) 
        assert login_page.get_message() == f"Enjoy your vacation, {first_name} {last_name}!"
       



