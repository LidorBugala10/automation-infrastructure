import pytest
from playwright.sync_api import Playwright
from smart_assertions import soft_assert,verify_expectations
user_name = "standard_user"
password = "secret_sauce"
first_name= "Lidor"
last_name = "Bugala"
postal_code = "4580123456789"


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
        page.locator('[data-test="username"]').fill(user_name)
        page.locator('[data-test="password"]').fill(password)
        page.locator('[data-test="login-button"]').click()
        
        yield
        context.tracing.stop(path="trace.zip")
        page.close()
        context.close()
        browser.close()
        #playwright show-trace trace.zip

 

    def test01_verify_empty_cart_checkout(self):
        page.locator ('[data-test="shopping-cart-link"]').click()
        page.locator ('[data-test="checkout"]').click()
        page.locator ('[data-test="firstName"]').fill(first_name)
        page.locator ('[data-test="lastName"]').fill(last_name)
        page.locator ('[data-test="postalCode"]').fill(postal_code)
        page.locator ('[data-test="continue"]').click()
        actual_amount = float(page.locator("[data-test='subtotal-label']").inner_text().replace("Item total: $",""))
        page.locator ('[data-test="finish"]').click()
        soft_assert(actual_amount > 0,"Amount Should be greater than zero")
        verify_expectations()

    def test02_verify_image_and_description(self):
        real_text = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
        page.locator ('[alt="Sauce Labs Backpack"]')
        page.locator ('[data-test="inventory-item-name"]').first
        page.locator ('[data-test="inventory-item-desc"]').first
        actual_text = page.locator ('[data-test="inventory-item-desc"]').first.inner_text()
        assert real_text == actual_text

    def test03_verify_remove_product_from_cart(self):
        page.locator ('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        page.locator ('[data-test="shopping-cart-link"]').click()
        page.locator ('[data-test="remove-sauce-labs-backpack"]').click()
        assert page.locator('[data-test="remove-sauce-labs-backpack"]').count() == 0

  
    def test04_verify_product_added_to_cart(self):
        page.locator("[class='btn btn_primary btn_small btn_inventory ']").first.click()
        page.locator("[data-test='shopping-cart-link']").click()
        page.locator("[data-test='continue-shopping']").click()
        page.locator("[class='btn btn_primary btn_small btn_inventory ']").nth(1).click()
        assert page.locator("[data-test='shopping-cart-badge']").is_visible()
    
    
    def test05_verify_checkout_process(self):
        page.locator("[class='btn btn_primary btn_small btn_inventory ']").first.click()
        page.locator("[data-test='shopping-cart-link']").click()
        page.locator("[data-test='checkout']").click()
        page.locator("[data-test='firstName']").fill(first_name)
        page.locator("[data-test='lastName']").fill(last_name)
        page.locator("[data-test='postalCode']").fill(postal_code)
        page.locator("[data-test='continue']").click()
        page.locator("[data-test='finish']").click()
        header_text= page.locator("[data-test='complete-header']").inner_text()
        excepted_text =  "Thank you for your order!"
        assert header_text == excepted_text 

 
    def test06_verify_select_clothing_option(self):
        page.locator("[data-test='product-sort-container']").click()
        option ="[data-test='product-sort-container']"
        page.select_option(option,value='az')
        page.select_option(option,value='za')
        page.select_option(option,value='lohi')
        page.select_option(option,value='hilo')
        assert page.locator("[data-test='product-sort-container']").is_enabled()






        
        






   
   
        

   


        



