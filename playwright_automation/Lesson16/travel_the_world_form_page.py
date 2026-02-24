import allure
from playwright.sync_api import Page

class TravelTheWorldFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.choose_a_flight = page.locator('[type="submit"]')

    @allure.step("choose a flight")
    def choosen_flight(self):
        self.choose_a_flight.nth(0).click()
