import allure
import pytest
from playwright.sync_api import Playwright, expect
from playwright_automation.Lesson16.fun_kids_live import FunKidsLive
from playwright_automation.Lesson16.yum_website import YumMainPage


class TestFunKids:

    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page, fun_kids_live
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.funkidslive.com/learn/top-10-facts/top-10-facts-about-fish/")
        fun_kids_live = FunKidsLive(page)
        yield
        context.close()
        page.close()

    @allure.title("Test01- verify fish facts")
    @allure.description("This test verify the fish facts")
    def test01_verify_links(self):
        fun_kids_live.print_facts()
        assert fun_kids_live.get_total_facts() == 10
        
     