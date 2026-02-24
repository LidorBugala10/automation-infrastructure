import pytest
from playwright.sync_api import Playwright
class Test_Locator:
    @pytest.fixture(autouse=True, scope="class")
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(
            headless=False,
            channel="chrome",
            slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True  )
        
        yield

        page.close()
        context.close()
        browser.close()

    def test_controller(self):
        page.goto("https://playground.atidcollege.co.il/registration/index.html")
        header_text = page.locator("h1").text_content()
        print(f"\nThe header text is : {header_text}.")
        page.locator("#name").fill("Lidor Bugala")
        page.locator("#email").fill("lidor34@gamil.com")
        page.locator("#password").fill("1234567890")
        page.locator("[id='confirmPassword']").fill("1234567890")
        page.locator("#terms").check()
        page.locator("//*[@id='registrationForm']/button").click()

    def test_saucedemo(self): 
        page.goto("https://www.saucedemo.com")
        page.locator("id=user-name").fill("standard_user")
        page.locator("id=password").fill("secret_sauce")
        page.locator("id=login-button").click()
        products = page.locator(".inventory_item")
        print("\nNumber of products:", products.count())
        page.goto("https://www.saucedemo.com")
        









       