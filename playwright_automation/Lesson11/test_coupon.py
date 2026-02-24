import allure 
import pytest
from playwright.sync_api import Playwright, expect
from playwright_automation.Lesson11.test_atid_coupon_page import AtidCouponPage
class TestAtidPage:

    @pytest.fixture(autouse = True,scope="class")
    def setup(self,playwright:Playwright):
        global browser,context,page,fill_submit_form 
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/ex_frames_practice.html")
        fill_submit_form = AtidCouponPage(page)
         

        yield
        context.close()
        page.close()

    @allure.title("Test01 - verify login with coupon")
    @allure.description("This test performs login using a coupon inside a frame and verifies the alert massage")
    def test01_verify_login_with_coupon(self):
        fill_submit_form.fiil_and_submit_with_coupon("lidor","bugala")
        message = fill_submit_form.get_alert_message()
        assert "lidor bugala" in message     
        
         

   

