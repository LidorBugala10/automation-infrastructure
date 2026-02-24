import allure
import pytest
from playwright.sync_api import Playwright, expect
from playwright_automation.Lesson12.dark_side_form_page import AtidFormPage
from playwright_automation.Lesson12.dark_side_login_page import LoginPage




class TestAtidPo:

    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page, login_page,form_page
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/atid-form")
        login_page = LoginPage(page)
        form_page = AtidFormPage(page)
        yield
        context.close()
        page.close()


    @allure.title("Test01 - Verify Button is Displayed")
    @allure.description("This test perform login,fill form and then verify button is displayed")
    def test01_verify_button_displayed(self):
        login_page.sign_in("atidUser","atidPass")
        form_page.fill_form("lidor","bugala","israel")
        assert form_page.get_massage()=="Hello, lidor bugala! You are from Israel."
        assert form_page.get_header_massage()== "Welcome to the Dark Side!"
        