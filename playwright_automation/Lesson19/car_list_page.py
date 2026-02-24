from playwright.sync_api import Page
class CarListPage:

    def __init__(self,page:Page):
        self.available_cars = page.locator("//ul[@id='available-list']/li")
        self.selected_cars = page.locator("//ul[@id='selected-list']/li")
        self.disabled_cars = page.locator("//li[@data-disabled='true']")
        

  