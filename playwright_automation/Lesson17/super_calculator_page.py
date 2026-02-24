import allure 
import pytest
from playwright.sync_api import Playwright, expect,Page

class SuperCalculatorPage:
    def __init__(self,page:Page):
        self.page = page
        self.first_input = page.locator('[ng-model="first"]')
        self.operator_selector = ('[ng-model="operator"]')
        self.second_input = page.locator('[ng-model="second"]')
        self.go_button = page.locator('[id="gobutton"]')
        self.result = page.locator('[class="ng-binding"]').first()

    def multiply_input(self,first_number,second_number):
        self.first_input.fill(str(first_number))
        self.page.select_option(self.operator_selector,value="MULTIPLICATION")
        self.second_input.fill(str(second_number))
        self.go_button.click()
    
    

    def get_calculetor_result(self):
        result = float(self.result.inner_text())
        print(f"\nThe result is :{result}")
        return result
