import time
import allure
from appium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from extensions.mobile_actions import MobileActions
from extensions.mobile_verifications import MobileVerifications
from appium.webdriver.common.touch_action import TouchAction
from page_objects.mobile.to_do_list_page import ToDoListPage

class Mobile_flow:
    
    def __init__(self,driver):
        self.driver = driver
        self.to_do_list_page = ToDoListPage(driver)

    @allure.step("Add new task:")
    def add_task(self,text):
        MobileActions.type_text(self.driver, self.to_do_list_page.search_filed, text) 
        MobileActions.click(self.driver, self.to_do_list_page.add_task_button)
        # self.to_do_list_page.search(*self.search).send_keys(text)

    @allure.step("Get task name from list")
    def get_task_name(self):
        task_name = MobileActions.get_text(self.driver,self.to_do_list_page.task_added_name)
        print(f"\n task name: {task_name}")
        return task_name
    
    @allure.step("Clear all tasks from list")
    def delete_all_tasks(self):
        MobileActions.click(self.driver, self.to_do_list_page.clear_all_tasks_button)
        WebDriverWait(self.driver, 5).until(
        EC.invisibility_of_element_located(self.to_do_list_page.all_tasks))

    @allure.step("Fetch all visible tasks")
    def get_all_tasks(self):
        return self.driver.find_elements(*self.to_do_list_page.all_tasks)
    
    @allure.step("Fetch all completed tasks")
    def get_all_completed_tasks(self):
        return self.driver.find_elements(*self.to_do_list_page.all_completed_tasks)

    @allure.step("Toggle task status (Mark as Done)")
    def mark_task_as_completed(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.to_do_list_page.toggle_button)
        )
        action = TouchAction(self.driver)
        action.tap(btn).perform()
  
    @allure.step("Navigate to Completed tab and wait for list to refresh")
    def navigate_to_completed_tab(self):
        MobileActions.click(self.driver, self.to_do_list_page.completed_button)

    @allure.step("Click Clear Completed button")
    def clear_completed_task(self):
        MobileActions.click(self.driver, self.to_do_list_page.clear_completed_button)
        WebDriverWait(self.driver, 5).until(
        lambda d: len(d.find_elements(*self.to_do_list_page.all_tasks)) == 1 )

            
    @allure.step("Delete a single task")
    def delete_task(self):
        MobileActions.click(self.driver, self.to_do_list_page.delete_button)
        WebDriverWait(self.driver, 5).until(
            lambda d: len(d.find_elements(*self.to_do_list_page.all_tasks)) == 0
        )