import allure 
import pytest
from playwright.sync_api import Playwright, expect,Page

class TodoListPage:
    def __init__(self,page:Page):
        self.page = page
        self.page = page
        self.add_task_field = page.locator('[id="todoInput"]')
        self.add_button = page.locator('[onclick="addTodo()"]')
        self.chekbox_field = page.locator('[class="text-gray-700"]')

    def add_task(self,task):
        self.add_task_field.fill(task)
        self.add_button.click()

    def get_total_task(self):
       return self.chekbox_field.count()
    

      
        
        
            


        
             