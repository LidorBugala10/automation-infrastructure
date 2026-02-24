
from playwright.sync_api import Page
from automation_infrastructure.extensions.ui_actions import UIActions
from playwright_automation.Lesson21.grafana_login_page import GrafanaLoginPage



class GrafanaFlow:
    def __init__(self,page:Page):
        self.page = page
        self.grafana_login_page = GrafanaLoginPage(page)
        
    def sign_in(self,user_name,password)->None:
        UIActions.update_text(self.grafana_login_page.email_or_user_name_field,user_name)
        UIActions.update_text(self.grafana_login_page.password_field,password)
        UIActions.click(self.grafana_login_page.login_button)

    def skip_password_change(self):
        UIActions.click(self.grafana_login_page.skip_button)

    def text_after_sign_in(self):
        UIActions.get_text(self.grafana_login_page.text_after_sign_in)

        

       