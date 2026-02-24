from playwright.sync_api import Playwright, expect
import pytest
from playwright_automation.Lesson19.car_list_flow import CarFlows



class TestCars:

    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page,car_flows
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/interview-questions/car-lists/")
        #Init Page Objects:
        car_flows = CarFlows(page)
        yield
        context.close()
        page.close()

    # def test01_verify_all_cars_selected(self):
    #     original_total_selected_cars = car_flows.get_total_selected_cars()
    #     original_total_available_cars = car_flows.get_total_available_cars()
    #     car_flows.move_all_cars_to_selected_cars()
    #     assert car_flows.get_total_selected_cars() == original_total_selected_cars + original_total_available_cars

    def test01_verify_all_cars_selected(self):
        available_cars = car_flows.get_available_cars_list()
        car_flows.move_all_cars_to_selected_cars()
        assert car_flows.is_all_contained(available_cars)


    