# import pytest
# from playwright.sync_api import Playwright,expect
# from playwright_automation.Lesson05.support import Support
# class TestLoudev:


#     @pytest.fixture(autouse=True,scope="class")
#     def setup(self,playwright:Playwright):
#         global browser,context,page
#         browser = playwright.chromium.launch(headless=False,channel="chrome",slow_mo=500)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("http://loudev.com/")
#         yield
#         context.close()
#         page.close()


#     def test01_items(self):
#         support = Support()
#         support.verify_elements(page)




