import allure
import pytest
from playwright.sync_api import Playwright, expect
from playwright_automation.Lesson16.yum_website import YumMainPage


class TestYumPage:

    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page, yum_main
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.yum.com/wps/portal/yumbrands/Yumbrands")
        yum_main = YumMainPage(page)
        yield
        context.close()
        page.close()

    @allure.title("Test01- verify iconing")
    @allure.description("This test verify the iconic links")
    def test01_verify_links(self):
        yum_main.print_links()
        assert yum_main.get_total_links()==4








