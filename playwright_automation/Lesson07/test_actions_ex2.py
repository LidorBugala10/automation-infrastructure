from itertools import product
import pytest
from playwright.sync_api import Playwright
from smart_assertions import soft_assert,verify_expectations

from playwright_automation.Lesson04 import test_assert

class TestActionsEx2:

    @pytest.fixture(autouse=True, scope="function")
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
        page.goto ("https://atidcollege.co.il/Xamples/ex_actions.html")

       
        yield
        page.close()
        context.close()
        browser.close()

    def handle_alert(self, dialog):
        print("\nAlert text is: " + dialog.message)
        dialog.accept()    

    def test_verify_01(self):
        page.locator('[id="button1"]').click()
        frame1=page.frame_locator('[id="frame_a"]')
        frame1.locator ('[id="first_name"]').fill("Eli")
        frame1.locator ('[id="last_name"]').fill("Bugala")
        coupon = page.locator('[id="message-box"]').inner_text().replace("Your coupon code is: ","")
        frame1.locator ('[id="coupon"]').fill(coupon)
        page.once("dialog",lambda dialog: self.handle_alert(dialog))
        frame1.locator ('[onclick="showAlert()"]').click()
        
    def test_verify_02(self):
        draggable = '[id="draggable"]'
        droppable = '[id="droppable"]'
        page.drag_and_drop(draggable,droppable,force=True)
        drop_text = page.locator ('//*[@id="droppable"]/p').inner_text()
        print(f"\ndrop text is : {drop_text}")
        real_text = "Dropped!"
        assert drop_text == real_text

    def test_verify_03(self):
        items =page.locator("//ol[@id='select_items']/li")
        page.keyboard.down("Control")
        items.nth(1).click()
        items.nth(2).click()
        page.keyboard.up("Control")
        soft_assert("ui-selected" in items.nth(1).get_attribute("class"))
        soft_assert("ui-selected" in items.nth(2).get_attribute("class"))
        verify_expectations()


    def test_verify_04(self):
        page.locator('[id="dbl_click"]').dblclick()
        text= page.locator('[id="demo"]').inner_text()
        print(f"\nThe text is : {text}")
        assert text  == "Hello World",f"Error actual text is :{text}"


    def test_verify_04(self):
        page.locator('[id="mouse_hover"]').hover()
        new_color = page.locator("[id='mouse_hover']").get_attribute("style")
        assert new_color == "background-color: rgb(255, 255, 0);"

        
    def test_verify_05(self):
        elem = page.locator ('[id="scrolled_element"]')
        elem.scroll_into_view_if_needed()
        expected_text = "This Element is Shown When Scrolled"
        actual_text = elem.inner_text()
        print(f"\nThe actual text is :{actual_text}")
        assert actual_text == expected_text




       

        
    


        

        







       




    








    