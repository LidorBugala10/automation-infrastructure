import allure 
import pytest
from playwright.sync_api import Playwright, expect,Page

class GrafanaLoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.email_or_user_name_field = page.locator('[id=":r0:"]')
        self.password_field = page.locator('[id=":r1:"]')
        self.login_button = page.locator('[type="submit"]')
        self.skip_button = page.locator('[class="css-1riaxdn"]').nth(1)
        self.text_after_sign_in = page.locator('[class="css-1ti7uft"]')
