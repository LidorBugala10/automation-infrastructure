import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.asus.com/il/")
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="ZenBook 14 UX435").click()
    page.get_by_role("link", name="כל הסדרות").click()
    page.get_by_role("link", name="See all Zenbook Pro").click()
    page.get_by_role("link", name="LearnMore about ASUS Zenbook").click()
