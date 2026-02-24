from playwright.sync_api import Page
import allure
class YumMainPage:
    def __init__(self, page:Page):
        self.page = page
        self.links_id = page.locator("[class*='m-0 tgb']")

    def print_links(self):
        links = self.links_id.all()
        for link in links :
            print(link.get_attribute("href"))

    def get_total_links(self):
        total_link = len(self.links_id.all())
        print(f"total links:{total_link}")
        return total_link   



   


        