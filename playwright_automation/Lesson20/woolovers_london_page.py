import allure 
import pytest
from playwright.sync_api import Playwright, expect,Page

class WooloversLondonPage:
    def __init__(self,page:Page):
        self.page = page
        self.Allow_all_btn = page.locator('[id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
        self.Close_popup = page.locator('[class="glClose"]')
        self.New_in_item = page.locator('[class="dropdown hasSubmenu New In"]')
        self.Shoping_now_btn = page.locator('[id="ge_flagPrefix"]').first
        self.select_delivery_country ='[id="gle_selectedCurrency"]'
        self.confirm_btn = page.locator('[class="glDefaultBtn glCancelBtn"]')
        self.clear_all_btn = page.locator('[class="filters-current__item filters-current__item--clear text-uppercase"]').nth(2)
        self.select_gender = page.locator('[id="dd-Gender"]')
        self.select_male_gender = page.locator('[data-filter-id="160"]')
        self.Sort_by_btn = page.locator('[id="dd-Sort By"]')
        self.Sort_by_low_to_high = page.locator('[data-filter-id="1"]').nth(0)
        self.Sort_by_done_btn = page.locator('//div[10]/div/div/div[3]')
        



