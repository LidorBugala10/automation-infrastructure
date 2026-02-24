from typing import List
from playwright.sync_api import Page
from playwright_automation.Lesson19.car_list_page import CarListPage
from playwright_automation.Lesson21.grafana_home_page import GrafanHomePage
from playwright_automation.Lesson21.grafana_login_page import GrafanaLoginPage


class GrafanaFlow:
    def __init__(self,page:Page):
        self.page = page
        self.login = GrafanaLoginPage(page)
        self.home = GrafanHomePage(page)

    def sign_in(self,user_name:str,password:str)->None:
        self.login.email_or_user_name_field.fill(user_name)
        self.login.password_field.fill(password)    
        self.login.login_button.click()
        self.login.skip_button.click()
    
    def get_header(self)->str:
        header_text = self.home.header_element.inner_text()
        print(f"\nHeader Text:{header_text}")
        return header_text