from itertools import product
import pytest
from playwright.sync_api import Playwright
class TestProducts:

    @pytest.fixture(autouse=True, scope="class")
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(
            headless=False,
            channel="chrome",
            slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True  )
       
        yield
        page.close()
        context.close()
        browser.close()


    def test_verify_products(self):
        page.goto(" https://atidcollege.co.il/workshops/avengers/exercise/")
        avengers = page.locator("[width='25%']").all()
        for i in range(4):
            print(f"\n{i+1}-{avengers[i].inner_text()}")


    def test_playground(self):
        page.goto("https://playground.atidcollege.co.il/")
        page.locator ("[id ='username']").fill("user_basic") 
        page.locator ('[id="password"]').fill("secret")
        page.locator ('[id="login"]').click()
        page.locator ('[src="https://atidcollege.co.il/atid-club/assets/images/logo2.png"]')
       
 
       
        
        

    


        


    


