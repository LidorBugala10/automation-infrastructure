from playwright.sync_api import Page
class GrafanaLoginPage:
    def __init__(self,page:Page):
        self.email_or_username_field = page.locator('[id=":r0:"]')
        self.password_field = page.locator('[id=":r1:"]')
        self.skip_button = page.locator('[class="css-1riaxdn"]').nth(1)
        
        self.text_after_sign_in = page.locator('[class="css-1ti7uft"]')
        
        

        











        