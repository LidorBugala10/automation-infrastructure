
import allure
import pytest
from playwright.sync_api import Playwright
import xml.etree.ElementTree as ET



def get_data(node_name):
    root = ET.parse(r'playwright_automation\Lesson10\PIZZA_data.xml').getroot()
    return root.find(".//" + node_name).text  

Firat_Name =get_data("FIRST_NAME")
Last_name = get_data("LAST_NAME")
Phone_Number =get_data("PHONE_NUMBER")


class TestPizza:

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
        page.goto ("https://atidcollege.co.il/Xamples/pizza/")

       
        yield
        page.close()
        context.close()
        browser.close()

        
    @allure.step(f"Enter with First name :{Firat_Name},Last name {Last_name},and Phone number {Phone_Number}")
    def verify_login_page(Self,First_name,Last_name,Phone_Number):
        page.locator("[id='input_5_22_3']").fill(Firat_Name)
        page.locator("[id='input_5_22_6']").fill(Last_name)
        page.locator("[id='input_5_23']").fill(Phone_Number)

    @allure.step("Choose option:Original Hand Tossed Crust")
    def verify_select_option(self):
        page.locator("[name='input_27']").select_option("Original Hand Tossed Crust|0")
        page.locator('[id="gform_submit_button_5"]').click()


    @allure.title("Test - verify pizza order ")
    @allure.description("Verify successful order")
    def test_verify_pizza(self):
        self.verify_login_page(Firat_Name,Last_name,Phone_Number)
        self.verify_select_option()

        
        
       