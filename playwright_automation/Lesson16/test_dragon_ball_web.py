import allure
import pytest
from playwright.sync_api import Playwright, expect
from playwright_automation.Lesson16.dragon_ball_page import DragonBallWeb


class TestDragonBall:
    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page,  dragon_ball_web
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://web.dragonball-api.com/")
        dragon_ball_web = DragonBallWeb(page)
        yield
        context.close()
        page.close()

    @allure.title("Test01 - Verify all characters from Dragon Ball")
    @allure.description("This test scrolls to the bottom of the Dragon Ball page, prints all characters, and verifies the total count is correct.")
    def test01(self):
        dragon_ball_web.scroll_to_buttom()
        dragon_ball_web.print_characters()
        assert dragon_ball_web.get_characters_count() == 58

