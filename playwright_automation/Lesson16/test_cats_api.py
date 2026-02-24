import json
import pytest
from playwright.sync_api import Playwright,Page
import requests
from smart_assertions import soft_assert,verify_expectations
import requests

cat_url = "https://api.thecatapi.com/v1/images/search"

class Test_Api_Cats_Website:
    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global request_context,page 
        request_context=playwright.request.new_context(base_url=cat_url)
        yield
        request_context.dispose()

    def test01_verify_a_cat_image(self,page:Page):
        response = requests.get(cat_url) 
        data = response.json()  
        cat_img_url = data[0]['url']
        print(f"\nThis is a cat img :{cat_img_url}")
        page.goto(cat_img_url)
        page.locator("//img").screenshot(path="cat_image.png")
        print("The image was saved as cat_image.png")
        
