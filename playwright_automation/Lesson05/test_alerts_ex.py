import pytest
from playwright.sync_api import Playwright
class TestAlertEx:

    @pytest.fixture(autouse=True, scope="class")
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(
            headless=False,
            channel="chrome",
            slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True  )
        yield
        page.close()
        context.close()
        browser.close()
        

    def test01(self):
        first_name = "Lidor"
        last_name = "Bugala"
        page.goto("https://atidcollege.co.il/Xamples/ex_frames_practice.html")
        frame = page.frame_locator('[id="frame_a"]')
        frame.locator('[id="button1"]').click
        frame.locator('[id="first_name"]').fill(first_name)
        frame.locator ('[id="last_name"]').fill(last_name)
        coupon = frame.locator('[id="message-box"]').inner_text()
        frame.locator('[id="coupon"]')
        print("Coupon dynamically copied:", coupon)
        page.on("dialog", lambda dialog:(print("Alert text :",dialog.massage), dialog.accept()))




