import allure
import pytest
from playwright.sync_api import Playwright, expect

keyword = "search_value,expected_result"
data = [("smart","2"),
        ("blender","1"),
        ("phone","2"),
        ("kuku","No")]
        



class TestParametrize:

    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page, login_page,form_page
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://playground.atidcollege.co.il/product-explorer/index.html")
        yield
        context.close()
        page.close()

    
    @pytest.mark.parametrize(keyword,data)
    def test01_playground(self,search_value,expected_result):
        page.locator('[id="searchInput"]').fill(search_value)
        actual_text = page.locator('[id="resultsCount"]').inner_text()
        print(f"\nThe actual text is:{actual_text}")
        assert expected_result in actual_text

        




        
