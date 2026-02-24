import allure 
from playwright.sync_api import Page

class AtidLoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.first_name_field = page.locator("[id='not-random']")
        self.Last_name_field = page.locator("[type='text']").nth(1)
        self.destination_selector = "[id='destinationType']"
        self.check_box = page.locator('[type="checkbox"]').first
        self.radio_button = page.locator('[type="radio"]').nth(1)
        self.submit_button = page.locator("[type='submit']")
        self.message_element = page.locator("[id='successMessage']")

    @allure.step("Sign in:")
    def sign_in(self,first_name,Last_name,destination_Type):
        self.first_name_field.fill(first_name)
        self.Last_name_field.fill(Last_name)
        self.page.select_option(self.destination_selector,value=destination_Type)
        self.check_box.click()
        self.radio_button.click()
        self.submit_button.click()  

    def get_message(self):
        message = self.message_element.inner_text().replace("\n","")
        print(f"\nThe message is: {message}")
        return message