import allure
import pytest
from playwright.sync_api import Playwright, expect
from playwright_automation.Lesson16.purchase_the_flight import TravelTheWorldPurchasePage
from playwright_automation.Lesson16.travel_the_world_form_page import TravelTheWorldFormPage
from playwright_automation.Lesson16.travel_the_world_page import TravelTheWorldPage




class TestTravelTheWorld:
    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page, purchase_the_flight,choose_city,choosen_flight,purchase_flight
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://blazedemo.com/")
        purchase_the_flight = TravelTheWorldPurchasePage(page)
        choose_city=TravelTheWorldPage(page)
        choosen_flight=TravelTheWorldFormPage(page)
        purchase_flight = TravelTheWorldPurchasePage(page)
        yield
        context.close()
        page.close()

    @allure.title("Test01 - Verify Button is Displayed")
    @allure.description("This test perform login,fill form and then verify button is displayed") 
    def test01_verify_button_displayed(self):
        choose_city.select_option("Paris","London")
        choosen_flight.choosen_flight()
        purchase_flight.purchase_flight( "Lidor Bugala",
        "1 Main Street",
        "Tel Aviv",
        "Center",
        "12345",
        "Visa",
        "4111111111111111",
        "12",
        "2028",
        "Lidor Bugala",
        )

        text_after_purchase = page.locator("//h1").inner_text()
        print(f"\nThe Text After Purchase is : {text_after_purchase}")
        assert text_after_purchase == "Thank you for your purchase today!"
        

