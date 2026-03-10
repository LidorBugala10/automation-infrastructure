from playwright.sync_api import Page
class GrafanaPluginsPage:
    def __init__(self,page:Page):
        self.administration_button = page.locator("//p[text()='Administration']")
        self.plugins_and_data_button = page.locator('[class="css-111zz4r"]').nth(1)
        self.plugins_button = page.locator("//a[text()='Plugins']")
        self.plugins_search_field = page.locator('[type="text"]').nth(0)
        self.google_apps = page.locator('[class="css-1stwewm plugin-name"]')


        