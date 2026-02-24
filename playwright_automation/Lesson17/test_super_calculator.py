import random
import time
import allure
import pytest
from playwright.sync_api import Playwright,expect
from playwright_automation.Lesson17.super_calculator_page import SuperCalculatorPage


class TestCalculatorPage:
    @pytest.fixture(autouse=True, scope="class")
    def setup(self, playwright: Playwright):
        global browser, context, page, calculator_page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://juliemr.github.io/protractor-demo/")
        calculator_page = SuperCalculatorPage(page)
        yield
        context.close()
        page.close()

    @allure.title("Calculate sum of random number using calculator")
    def test_calculator_random_number(self):
        calculator_page.multiply_input(3,2)
        time.sleep(3)
        assert calculator_page.get_calculetor_result()==3*2
      

       