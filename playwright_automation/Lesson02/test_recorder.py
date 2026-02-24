import pytest
from playwright.sync_api import Playwright


class TestRecorder:

    @pytest.fixture(autouse=True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page
        browser = playwright.chromium.launch(headless=False,channel="chrome",slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/bmi/")
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield 

        context.tracing.stop(path="trace.zip")
        context.close()
        page.close() 
        
    def test_example(self):
        page.locator("#weight").click()
        page.locator("#weight").fill("70")
        page.locator("#hight").click()
        page.locator("#hight").fill("178")
        page.get_by_role("button", name="Calculate BMI").click()
        page.get_by_role("button", name="Reset").click()