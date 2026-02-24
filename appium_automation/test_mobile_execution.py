import time
from appium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class TestAppiumExecution:
    
    @pytest.fixture(autouse = True,scope="class")
    def setup(self):
        global driver
        dc = {}
        dc['udid'] = 'ce051605b5d4d82c03'
        dc['appPackage'] = 'io.appium.android.apis'
        dc['appActivity'] = '.ApiDemos'
        dc['platformName'] = 'android'
        driver = webdriver.Remote('http://localhost:4723/wd/hub',dc)
        driver.implicitly_wait(10)
        yield
        time.sleep(3)
        driver.quit()


    def test01_verify_execution(self):
        list = driver.find_elements(By.XPATH,"//*[@id='text1']")
        assert len(list) == 12

    def test02_verify_width_and_height(self):
        element = driver.find_element(By.XPATH,"//*[@text='Content']")
        size = element.size
        print(f"\nWidth:", size['width'])
        print("Height:", size['height'])
        location = element.location
        print("X:", location['x'])
        print("Y:", location['y'])

    def test03_verify_activity(self):
      activity = driver.current_activity
      print(f"\nThe current activity is : {activity}")
      time = driver.get_device_time()
      print(f"The time is :{time}")


    def test04_verify_application(self):
        application_name = "EriBank"
        is_installed = driver.is_app_installed("com.EriBank")
        print(f"\nIs app installed?", is_installed)
        assert is_installed , f"The application  {application_name} Not installed on the device"
        pass 


    def test05_verify_orientation(self):
        orientation = driver.orientation
        print(f"\nCurrent Orientation:", orientation)
        if orientation == "PORTRAIT":
            print("Device is in PORTRAIT mode")
        else:
            print("Device is in LANDSCAPE mode") 


    def test06_verify_screenshot(self):
        screenshot1 = driver.get_screenshot_as_file("notification_screen.png")
        print(f"\nNotification screenshot saved:",screenshot1)
        driver.press_keycode(3)
        time.sleep(2)
        screenshot2 = driver.get_screenshot_as_file("home_screen.png")
        print("Home screenshot saved:", screenshot2)
        driver.quit()


        
        










        




        