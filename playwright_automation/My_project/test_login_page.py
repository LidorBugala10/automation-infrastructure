import pytest
from playwright.sync_api import Playwright

user_name = "standard_user"
password = "secret_sauce"


class TestSauceDemo:

    @pytest.fixture(autouse=True, scope="function")
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(
            headless=False,
            channel="chrome",
            slow_mo=900)
        context = browser.new_context()
        page = context.new_page()
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True  )
        page.goto("https://www.saucedemo.com/")
        
        yield
        context.tracing.stop(path="trace.zip")
        page.close()
        context.close()
        browser.close()
        #playwright show-trace trace.zip

        
    def test07_verify_login_success(self):
            header_text = "Swag Labs"
            page.locator('[data-test="username"]').fill(user_name)
            page.locator('[data-test="password"]').fill(password)
            page.locator('[data-test="login-button"]').click()
            actual_text = page.locator('[class="app_logo"]').inner_text()
            assert actual_text == header_text
            
    def test08_verify_login_invalid_creds(self):
            user_name = "123456789"
            password = "&&&***"
            error_message ="Epic sadface: Username and password do not match any user in this service"
            page.locator('[data-test="username"]').first.fill(user_name)
            page.locator('[data-test="password"]').fill(password)
            page.locator('[data-test="login-button"]').click()
            actual_text = page.locator('[data-test="error"]').inner_text()
            assert actual_text == error_message 
        
    def test09_verify_login_with_multiple_users(self):
        users = ["standard_user", "problem_user", "performance_glitch_user"]
        password = "secret_sauce"
        for user in users:
            page.locator('[data-test="username"]').first.fill(user)
            page.locator('[data-test="password"]').fill(password)
            page.locator('[data-test="login-button"]').click()
            last_url = page.url
            page.locator('[id = react-burger-menu-btn]').click()
            page.locator('[id = logout_sidebar_link]').click()
            assert "inventory.html" in last_url

    def test10_verify_logout(self):
        page.locator("[data-test='username']").fill(user_name)
        page.locator("[data-test='password']").fill(password)
        page.locator("[data-test='login-button']").click()
        page.locator("[id='react-burger-menu-btn']").click()
        page.locator("[id='logout_sidebar_link']").click()
        assert page.url == "https://www.saucedemo.com/"