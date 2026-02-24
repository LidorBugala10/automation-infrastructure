import pytest
from playwright.sync_api import Playwright


class Test_Browsers_Connection:

    @pytest.fixture(autouse=True, scope="class")
    def setup(self, playwright: Playwright):
        global browser, context, page

        browser = playwright.chromium.launch(
            headless=False,
            channel="msedge",
            slow_mo=500
        )

        context = browser.new_context()
        page = context.new_page()

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        yield

        page.close()
        context.close()
        browser.close()

    def test_to_microsift_edge(self):
        page.goto("https://www.google.com")
        page.goto("https://www.bing.com")
        page.go_back()

      
        






        