import allure
from playwright.sync_api import Page

class TravelTheWorldPurchasePage:
    def __init__(self, page: Page):
        self.page = page
        self.full_name_field = page.locator('[id="inputName"]')
        self.address_field = page.locator('[id="address"]')
        self.city_field = page.locator('[id="city"]')
        self.state_field = page.locator('[id="state"]')
        self.zip_code_field = page.locator('[id="zipCode"]')
        self.card_type_selector = page.locator('[id="cardType"]')
        self.credit_card_number_field = page.locator('[id="creditCardNumber"]')
        self.month_field = page.locator('[id="creditCardMonth"]')
        self.year_field = page.locator('[id="creditCardYear"]')
        self.name_on_card_field = page.locator('[id="nameOnCard"]')
        self.remember_me_check_box = page.locator('[id="rememberMe"]')
        self.purchase_flight_button = page.locator('[class="btn btn-primary"]')


    @allure.step("choose a flight")
    def purchase_flight(self,full_name,address,city,state,zip_code,payment_option,credit_card_number,month,year,name_on_card):
        self.full_name_field.fill(full_name)
        self.address_field.fill(address)
        self.city_field.fill(city)
        self.state_field.fill(state)
        self.zip_code_field.fill(zip_code)
        self.card_type_selector.select_option(payment_option)
        self.credit_card_number_field.fill(credit_card_number)
        self.month_field.fill(month)
        self.year_field.fill(year)
        self.name_on_card_field.fill(name_on_card)
        self.remember_me_check_box.check()
        self.purchase_flight_button.click() 



