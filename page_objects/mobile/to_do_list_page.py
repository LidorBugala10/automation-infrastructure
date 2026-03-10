import time
from appium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class ToDoListPage:

    def __init__(self,driver):
        self.driver = driver
        self.search_filed = (By.XPATH, "//*[@id='todo-input']")
        self.add_task_button = (By.XPATH,"//*[@text='Add Task']")
        self.task_added_name = (By.XPATH, "//*[@text='Buy Milk']")
        self.clear_all_tasks_button = (By.XPATH, "//*[@id='clear-all']")
        self.all_tasks = (By.XPATH, "//android.widget.ListView/android.view.View")
        self.toggle_button = (By.XPATH, "//*[@text='Toggle']")
        self.completed_button = (By.XPATH, "//*[@id='filter-completed']")
        self.all_completed_tasks = (By.XPATH, "//*[@class='android.view.View' and ./*[@text='clean the house']]")
        self.delete_button = (By.XPATH, "//*[@text='Delete']")
        self.clear_completed_button = (By.XPATH, "//*[@text='Clear Completed']")


        
