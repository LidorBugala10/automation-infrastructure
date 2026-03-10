import time
import allure
from appium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from data.mobile.mobile_ata import *
from extensions.mobile_verifications import MobileVerifications
from workflows.mobile.mobile_flow import Mobile_flow




class TestToDoList:
        
    @allure.title("Verify adding a new task")  
    @allure.description("Test that a user can successfully add a new task to the list")
    def test_verify_task_added(self,mobile_flow:Mobile_flow):
        mobile_flow.add_task(TASK_NAME)
        MobileVerifications.strings_are_equal(mobile_flow.get_task_name(),TASK_NAME)

    @allure.title("Verify Clear All Tasks")
    @allure.description("Test that the 'Clear All Tasks' button removes everything")
    def test_verify_all_tasks_cleared(self,mobile_flow:Mobile_flow):
        mobile_flow.delete_all_tasks()
        MobileVerifications.list_size(mobile_flow.get_all_tasks() , EXPECTED_TASK_COUNT_AFTER_CLEAR_ALL )

    @allure.title("Verify Single Task Deletion")
    @allure.description("Test that clicking Delete on a specific task removes it from the list")
    def test_verify_task_deletion(self, mobile_flow: Mobile_flow):
        mobile_flow.delete_all_tasks()
        mobile_flow.add_task(SEC_TASK_NAME)
        mobile_flow.delete_task()
        MobileVerifications.list_size(mobile_flow.get_all_tasks() , EXPECTED_TASK_COUNT_AFTER_DELETION)


    @allure.title("Verify Clear Completed Functionality")
    @allure.description("Verify that 'Clear Completed' button removes only completed tasks")
    def test_verify_clear_completed_functionality(self, mobile_flow: Mobile_flow):
            mobile_flow.delete_all_tasks()
            mobile_flow.add_task(TASK_NAME)
            mobile_flow.add_task(SEC_TASK_NAME)
            mobile_flow.mark_task_as_completed()
            mobile_flow.clear_completed_task()
            MobileVerifications.list_size(mobile_flow.get_all_tasks() , EXPECTED_ACTIVE_TASKS_COUNT)

    @allure.title("Verify task is moved to Completed list")
    @allure.description("Test that clicking Toggle marks the task as completed and moves it to the Completed list while keeping it in the main list")
    def test_verify_task_marked_as_completed(self, mobile_flow: Mobile_flow):
            mobile_flow.delete_all_tasks()
            mobile_flow.add_task(SEC_TASK_NAME)
            mobile_flow.mark_task_as_completed()
            mobile_flow.navigate_to_completed_tab()
            MobileVerifications.list_size(mobile_flow.get_all_completed_tasks() , EXPECTED_COMPLETED_TASKS_COUNT)