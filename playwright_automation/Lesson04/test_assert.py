import pytest
from playwright.sync_api import Playwright
class TestAsseretEx:

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


    def test_practice_form(self):
        page.goto("https://atidcollege.co.il/Xamples/practice-form.html")
        first_name = "Lidor"
        last_name = "Bugala"
        page.locator("#not-random").fill(first_name)
        page.locator('[type="text"]').nth(1).fill(last_name)
        page.locator('[name="destinationType"]').select_option("city")
        page.locator('[name="travelBuddy"]').check()
        page.locator('[name="dealPreference"]').first.check()
        page.locator('.submit-btn').click()
        expected_text = f"Enjoy your vacation, {first_name} {last_name}!"
        actual_text = page.locator('#successMessage h3').inner_text()
        assert actual_text == expected_text
        
    def test_navigate_to_atid_product(self):
        page.goto("https://playground.atidcollege.co.il/checkout-flow/index.html")  
        print("\nProducts list:")
        products = page.locator ("[class='font-medium text-lg mb-2']")
        for i in range(products.count()):
            print(products.nth(i).inner_text())
        prices = page.locator ("[class='text-gray-600 mb-4']")
        total = 0.0
        for i in range(prices.count()):
            price_text = prices.nth(i).inner_text()   
            price_number = float(price_text.replace("$",""))
            total += price_number
        print("\nTotal price:", total) 
        expected_total = 419.97
        assert total == expected_total
        

    def test_navigate_02(self):
        page.goto("https://playground.atidcollege.co.il/product-explorer/index.html")
        page.locator('[id="categoryFilter"]').select_option("Electronics")
        products = page.locator('[class="text-lg font-semibold text-gray-800 mb-1"]')
        for i in range(products.count()):
            print(products.nth(i).inner_text())
        
        prices = page.locator ("[class='text-xl font-bold text-indigo-600']")
        total = 0.0
        for i in range (prices.count()):
            price_text= prices.nth(i).inner_text()
            price_number = float(price_text)
            total+= price_number
        print("\n Total price:",total)
       
            

     

















   


  