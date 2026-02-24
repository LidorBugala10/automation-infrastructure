import allure
from playwright.sync_api import Page

class SauceDemoFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_product_to_cart = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.cart = page.locator("[data-test='shopping-cart-link']")
        self.cart_whit_product = page.locator('[data-test="shopping-cart-badge"]')
        self.all_products = page.locator('[data-test="inventory-item-name"]')
        self.product_price = page.locator('[data-test="inventory-item-price"]')
        self.description = page.locator('[data-test="inventory-item-desc"]')

    @allure.step("Add product to cart and open cart")
    def add_prodect(self):
        self.add_product_to_cart.click()
        self.cart.click()

    def get_cart_with_product(self):
        return self.cart_whit_product.inner_text()
    
    def get_all_products(self):
        # count = self.all_products.count()
        # print(f"Total products found: {count}")
        # for i in range(count):
        #     product_text = self.all_products.nth(i).inner_text()
        #     print(f"{i+1} - {product_text}")

         count = len(self.all_products.all())
         print(f"\nTotal products found: {count}")
         for i in range(count):
            product_text = self.all_products.all()[i].inner_text()
            print(f"{i+1} - {product_text}")

    def get_all_products_price(self):
        price = len(self.product_price.all())
        print(f"\nTotal price found is :{price}")
        for i in range(price):
            actual_price= self.product_price.all()[i].inner_text()
            print(f"{i+1} - {actual_price}")

    def get_all_description(self):
        description = len(self.description.all())
        print(F"\nThe descpritions of thr protucts is :{description}")
        for i in range(description):
            actual_desctiption =  self.description.all()[i].inner_text()
            print(f"{i+1} - {actual_desctiption}")          

 
        
        
        
       
        

       


       
      