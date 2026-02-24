from itertools import product
import pytest
from playwright.sync_api import Playwright
import xml.etree.ElementTree as ET



def get_data(node_name):
    root = ET.parse(r'playwright_automation\Lesson10\BMI_data.xml').getroot()
    return root.find(".//" + node_name).text  

weight = get_data("WEIGHT")
height = get_data("HEIGHT")
excepted_BMI = get_data("EXPECTED_BMI")

class TestBmiCalculator:

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
        page.goto ("https://atidcollege.co.il/Xamples/bmi/")

       
        yield
        page.close()
        context.close()
        browser.close()

    def test_verify_BMI(self):
        page.locator("[id='weight']").fill(weight)
        page.locator ('[id="hight"]').fill(height)
        page.locator ('[id="calculate_data"]').click()
        real_text = page.locator ('[id="bmi_result"]').input_value()
        print(f"\nThe BMI is :{real_text}")
        assert real_text == (excepted_BMI)



