import allure
from playwright.sync_api import Page

class TravelTheWorldPage:
    def __init__(self, page: Page):
        self.page = page
        self.city_departure = page.locator('[name="fromPort"]')
        self.city_destination = page.locator('[name="toPort"]')
        self.find_flights_button = page.locator('[type="submit"]') 

    @allure.step("Select departure city and destination city")
    def select_option(self, from_city, to_city):
        self.city_departure.select_option(label=from_city)
        self.city_destination.select_option(label=to_city)
        self.find_flights_button.click()
