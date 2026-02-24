from playwright.sync_api import Page
from playwright_automation.Lesson20.woolovers_london_page import WooloversLondonPage


class WooloversLondonFlow:
    def __init__(self, page: Page):
        self.page = page
        self.woolovers_london_page = WooloversLondonPage(page)

    def close_popups(self):
        self.woolovers_london_page.Allow_all_btn.click()
        self.woolovers_london_page.Close_popup.click()

    def go_to_new_in(self):
        self.woolovers_london_page.New_in_item.click()

    def change_currency_to_usd(self):
        self.woolovers_london_page.Shoping_now_btn.click()
        self.page.select_option(self.woolovers_london_page.select_delivery_country,value="USD")
        self.woolovers_london_page.confirm_btn.click()

    def clear_all(self):
        self.woolovers_london_page.clear_all_btn.click()  


    def select_man_gender(self):
        self.woolovers_london_page.select_gender.click()
        self.woolovers_london_page.select_male_gender.click()    

    def sort_price_low_to_high(self):
        self.woolovers_london_page.Sort_by_btn.click()
        self.woolovers_london_page.Sort_by_low_to_high.click()
        self.woolovers_london_page.Sort_by_done_btn.click()

   

    