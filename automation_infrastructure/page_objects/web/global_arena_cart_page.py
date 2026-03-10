from playwright.sync_api import Page
class GlobalArenaCartPage:
    def __init__(self,page:Page):
        self.evnet_message = page.locator('[style="font-weight: 700;"]')
        self.proceed_to_checkout = page.locator("//button[text()='Proceed to Checkout']")
        self.first_name_field = page.locator('[name="first_name"]')
        self.last_name_field =  page.locator('[name="last_name"]')
        self.email_address_field = page.locator('[name="email"]')
        self.phone_number_field = page.locator('[name="phone"]')
        self.street_address_field = page.locator('[name="street"]')
        self.city_field = page.locator('[name="city"]')
        self.zip_code_field = page.locator('[name="zip"]')
        self.card_number_field = page.locator('[name="card_number"]')
        self.expiry_date_field = page.locator('[name="expiry"]')
        self.cvv_field = page.locator('[name="cvv"]')
        self.check_box_button = page.locator('[type="checkbox"]')
        self.complete_purchase = page.locator('[id="checkout-btn"]')
        self.confirm_message = page.locator("//h1[text()='Order Confirmed!']")
        self.back_to_home_button = page.locator('//*[@id="thank_you"]/div/button')
        self.home_page_identifier = page.locator('[class="logo"]').first


