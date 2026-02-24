from playwright.sync_api import Page
class GrafanHomePage:
    def __init__(self,page:Page):
        self.header_element = page.locator('[class="css-1ti7uft"]')
