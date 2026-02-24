import pytest
from playwright.sync_api import Playwright
class Test_Locator:
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

    # def test_locator_navigate_saucedemo(self):
    #     page.goto("https://www.saucedemo.com")
    #     elem1= page.locator('[class="login_logo"]')
    #     elem1.click()
    #     elem2= page.locator('[class="form_group"]').first
    #     elem2.click()
    #     elem3 = page.locator('[class="form_group"]').nth(1)
    #     elem3.click()
    #     elem4 = page.locator ('[class="submit-button btn_action"]')
    #     elem4.click()

    # def test_locator_navigate_atid(self):
    #     page.goto("https://atidcollege.co.il/workshops/avengers/exercise/")
    #     page.locator("[id='iron_man']")
    #     page.locator("[id='captain_america']")
    #     page.locator("[id='the_hulk']")
    #     page.locator("[id='thor']")
    #     images= page.locator("img").count()
    #     print(f"\nThe Number Of Images is : {images}")

    # def test_locator_navigate_atid(self):
    #     page.goto("https://atidcollege.co.il/Xamples/ex_locators.html")

    #     page.locator("[id='locator_id']").click()
    #     print(page.locator("[id='locator_id']").text_content())

    #     page.locator("[name='locator_name']").click()
    #     print(page.locator("[name='locator_name']").text_content())

    #     page.locator("//*[@id='contact_info_left']/p").click()
    #     print(page.locator("//*[@id='contact_info_left']/p").text_content())

    #     page.locator("[class='locator_class']").click()
    #     print(page.locator("[class='locator_class']").text_content())


    #     page.locator("//*[@id='contact_info_left']/a[1]").click()
    #     print(page.locator("//*[@id='contact_info_left']/a[1]").text_content())

    #     page.locator("//*[@id='contact_info_left']/a[2]").click()
    #     print(page.locator("//*[@id='contact_info_left']/a[2]").text_content())

    #     page.locator("[myname='selenium']").click()
    #     print(page.locator("[myname='selenium']").input_value())

        
    #     page.locator("//*[@id='contact_info_left']/button").first.click()
    #     print(page.locator('//*[@id="contact_info_left"]/button').text_content())
        
        





