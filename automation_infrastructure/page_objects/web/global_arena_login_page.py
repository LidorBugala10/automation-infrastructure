from playwright.sync_api import Page
class GlobalArenaLoginPage:
    def __init__(self,page:Page):
        self.login_link = page.locator("//a[text()='Login']")
        self.login_user_name_input = page.locator('[id="username"]')
        self.login_password_input  = page.locator('[id="password"]')
        self.login_submit_button  = page.locator('[type="submit"]').nth(1)
        self.register_toggle_button  = page.locator('[onclick="toggleAuthMode()"]')
        self.register_user_name_input  = page.locator('[id="username"]')
        self.register_password_input  = page.locator('[id="password"]')
        self.register_submit_button  = page.locator('[type="submit"]').nth(1)
        self.logout_link = page.locator('[onclick="logout()"]')
