import allure 
import pytest
from playwright.sync_api import Playwright, expect,Page

class SauceDemoMyCartPage:
    def __init__(self,page:Page):
        self.page = page
        self.remove_product =page.locator('[data-test="remove-sauce-labs-backpack"]')

    @allure.step("remove product from cart")
    def remove_prodect(self):
        self.remove_product.click()
           