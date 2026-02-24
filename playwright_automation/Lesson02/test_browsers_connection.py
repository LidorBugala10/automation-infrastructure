import pytest
from playwright.sync_api import Playwright


class Test_Browsers_Connection:

    @pytest.fixture(autouse=True, scope="class")
    def setup(self, playwright: Playwright):
        global browser, context, page

        browser = playwright.chromium.launch(
            headless=False,
            channel="chrome",
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




        

    def test_go_to_wikipedia(self):
         page.goto("https://www.wikipedia.org/")
         elem1 = page.locator("[class='footer-sidebar-content']").first
         elem2 = page.locator ("[id='search-input']")
         elem3 = page.locator("[id='searchLanguage']")
         elements = [elem1,elem2,elem3]
         for elem in elements :
            print(f"\n The element is :{elem}")



     

    # def test_connection_browsers(self):
    #     page.goto("https://www.imdb.com")

    #     title_page = page.title()
    #     expected_title = "IMDb"

    #     if title_page == expected_title:
    #         print("YES! Title is correct")
    #     else:
    #         print("NO! Title is not correct")

    #     current_url = page.url
    #     expected_url = "https://www.imdb.com/"

    #     if current_url == expected_url:
    #         print("URL is correct!")
    #     else:
    #         print("URL is not correct!")

    # def test_locator_by_class(self):
    #     page.goto("https://playwright.dev")
    #     logo_image = page.locator(".navbar__brand img")
    #     image_src = logo_image.get_attribute("src")
    #     print("\n Image path:", image_src)
    #     images = page.locator("a").count()
    #     print(f"\n The number of links in page is {images}")




       







       

        




                  

      



   

