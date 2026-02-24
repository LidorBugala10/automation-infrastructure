import allure
import pytest
from playwright.sync_api import Playwright
import xml.etree.ElementTree as ET

name = "Lidor"
subject = "help with my card"
Email = "lidorbugala.12@gmail.com"
Message = "My card is not working ,i dont know why"


class TestAtidStore:

    @pytest.fixture(autouse=True, scope="function")
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
        page.goto ("https://atid.store/contact-us/")

       
        yield
        page.close()
        context.close()
        browser.close()


    @allure.step(F"Enter your name :{name},subject:{subject},Email:{Email},and your massage: {Message}")
    def verify_send_message_to_contact(self,name,subject,Email,Massage):
        page.locator("[id='wpforms-15-field_0']").fill(name)
        page.locator("[id='wpforms-15-field_5']").fill(subject)
        page.locator("[id='wpforms-15-field_4']").fill(Email)
        page.locator("[id='wpforms-15-field_2']").fill(Message)
        page.locator("[id='wpforms-submit-15']").click() 

    @allure.step("verify the contact us page")
    def verify_contact_us_page(self):
        actual_text=page.locator("[id='wpforms-confirmation-15']").inner_text()
        print(f"\nThe actual text is : {actual_text}")
        assert actual_text == "Thanks for contacting us! We will be in touch with you shortly."


    @allure.title("Test01 - verify contact us page")
    @allure.description("This test included sending a message on the Contact Us page and verifying")
    def test_verify_contact_us(self):
        self.verify_send_message_to_contact(name,subject,Email,Message)
        self.verify_contact_us_page()






