# import allure
# import pytest
# from playwright.sync_api import Playwright, expect




# class TestAtidPo:

#     @pytest.fixture(autouse = True,scope="class")
#     def setup(self,playwright:Playwright):
#         global browser,context,page,todo_page
#         browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://atidcollege.co.il/Xamples/atid-form")
#         todo_page = PlayGroundPage(page)
#         yield
#         context.close()
#         page.close()


#     @allure.title("Test01 - Verify Button is Displayed")
    
#     @allure.description("This test perform login,fill form and then verify button is displayed")