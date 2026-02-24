import time
import allure
from playwright.sync_api import Page

class FishTankMarketFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.Names_of_all_products = page.locator('[class="product-title"]')
        self.Prices_of_all_products = page.locator('[class="price"]')
        self.product_names_count = page.locator('[class="product-title"]')
        self.products_prices_count = page.locator('[class="price"]')
        

    @allure.step("Verify all product names:")
    def get_all_product_names(self):
        time.sleep(5)
        count = len(self.Names_of_all_products.all())
        print(f"\nThe all products name is :{count}")
        for i in range(count):
            product_name = self.Names_of_all_products.all()[i].inner_text()
            print(f"\n{i+1} - {product_name}")
            

    @allure.step("Verify all product prices:")
    def get_all_products_prices(self):
        count = len(self.Prices_of_all_products.all())
        print(f"\nThe all products prices :{count}")
        for i in range(count):
            product_price = self.Prices_of_all_products.all()[i].inner_text()
            print(f"\n{i+1} - {product_price}")

    @allure.step("Verify all names and prices of all products: ")        
    def get_all_products_prices_and_names(self):
        self.product_names_count.count()
        self.products_prices_count.count()

