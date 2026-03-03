from playwright.sync_api import Page
class GrafanaLoginPage:
    def __init__(self,page:Page):
        self.search_field = page.locator('[id=":r0:"]')
        self.password_field = page.locator('[id=":r1:"]')
        self.login_button = page.locator("[class='css-1riaxdn']").first
        self.skip_button = page.locator("//span[text()='Skip']")   

        self.error_massage = page.locator('[data-testid="data-testid Alert error"]')
        self.text_after_sign_in = page.locator('[class="css-1ti7uft"]')
        self.login_page_header = page.locator("[class='css-1gmqqtf']")



        











        