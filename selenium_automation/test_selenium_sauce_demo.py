import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium_automation.sauce_data import *

class TestSeleniumSauceDemo:

    @pytest.fixture(autouse = True,scope="class")
    def setup(self):
        global driver,WebElement,webdriver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com/")
        yield
        time.sleep(3)
        driver.quit()

    def test01_verify_login(self):
        #Login Flow:
        user_name_field:WebElement = driver.find_element(By.CSS_SELECTOR,"[data-test='username']")
        user_name_field.send_keys("standard_user")

        password_field:WebElement = driver.find_element(By.ID,"password")
        password_field.send_keys("secret_sauce")

        click_button:WebElement = driver.find_element(By.NAME,"login-button")
        click_button.click()
        
        actual_header = driver.find_element(By.CSS_SELECTOR,"[data-test='title']").text
        print(f"\nActual Header:{actual_header}")
        assert actual_header == EXPECTED_HEADER


                                            
     