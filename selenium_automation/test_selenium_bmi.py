import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium_automation.bmi_data import *

class TestSeleniumBmi:
    @pytest.fixture(autouse = True,scope="class")
    def setup(self):
        global driver,WebElement,webdriver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://atidcollege.co.il/Xamples/bmi/")
        yield
        time.sleep(3)
        driver.quit()

    def test01_verify_bmi_calculate(self):
        weight_field:WebElement = driver.find_element(By.ID,'weight')
        weight_field.send_keys(WEIGHT)

        height_field:WebElement = driver.find_element(By.ID,'hight')
        height_field.send_keys(HEIGHT)

        calculate_bmi_button:WebElement =driver.find_element(By.ID,'calculate_data')
        calculate_bmi_button.click()

        bmi_after_calculate = driver.find_element(By.ID,'bmi_result').get_attribute("value")
        print(F"\nThe bmi after calculate is:{bmi_after_calculate}")
        assert bmi_after_calculate == BMI

