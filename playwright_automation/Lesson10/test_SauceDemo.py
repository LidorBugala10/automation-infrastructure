import allure
import pytest
from playwright.sync_api import Playwright
from smart_assertions import soft_assert,verify_expectations
import xml.etree.ElementTree as ET

def get_data(node_name):
    root = ET.parse(r'playwright_automation\Lesson10\PIZZA_data.xml').getroot()
    return root.find(".//" + node_name).text  


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

    @allure.step("")
    def test02_verify_image_and_description(self):
        real_text = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
        page.locator ('[alt="Sauce Labs Backpack"]')
        page.locator ('[data-test="inventory-item-name"]').first
        page.locator ('[data-test="inventory-item-desc"]').first
        actual_text = page.locator ('[data-test="inventory-item-desc"]').first.inner_text()
        assert real_text == actual_text
            

 