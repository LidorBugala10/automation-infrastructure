from playwright.sync_api import Playwright, expect
import pytest
from playwright_automation.Lesson19.car_list_flow import CarFlows
from playwright_automation.Lesson20.woolovers_london_flow import WooloversLondonFlow



class TestWooloversLondon:
    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page, Woolovers_London
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.wooloverslondon.com/")
        #Init Page Objects:
        Woolovers_London = WooloversLondonFlow(page)
        yield
        context.close()
        page.close()

    def test01(self):
        Woolovers_London.close_popups()
        Woolovers_London.change_currency_to_usd()
        Woolovers_London.go_to_new_in()
        Woolovers_London.clear_all()
        Woolovers_London.select_man_gender()
        Woolovers_London.sort_price_low_to_high() 
