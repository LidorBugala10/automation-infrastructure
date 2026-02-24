import allure 
import pytest
from playwright.sync_api import Playwright, expect,Page

class PlayGroundPage:
    def __init__(self,page:Page):
        self.page = page
        self.add_task_field = page.locator('[id="todoInput"]')
        self.add = page.locator('[onclick="addTodo()"]')
        self.chekbox_field = page.locator('[class="text-gray-700"]').all()
        self        

        
