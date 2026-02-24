import json
import pytest
from playwright.sync_api import Playwright
import requests
from smart_assertions import soft_assert,verify_expectations

chuck_api_url = "https://api.chucknorris.io/jokes/categories"
chuck_api_url_query1 = "https://api.chucknorris.io/jokes/search?query=barakobama"
chuck_api_url_query2 = "https://api.chucknorris.io/jokes/search?query=charliesheen"

class Test_Api_Chuck_Norris:
    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global request_context
        request_context=playwright.request.new_context(base_url=chuck_api_url)
        request_context = playwright.request.new_context(base_url=chuck_api_url_query1)
        request_context = playwright.request.new_context(base_url=chuck_api_url_query2)
        yield
        request_context.dispose()

    def test01_verify_random_jokes(self):
        response = request_context.get(url="random")
        print(response)
        print(json.dumps(response.headers,indent=2))
        joke_value=response=response.json()["value"]
        print(joke_value)
        assert response.status == 200

         
    def test02_verify_random_joke_from_category(self):
        api_params = {"category":"movie"}
        response = request_context.get(url="random",params=api_params)
        print(response)
        print(json.dumps(response.headers,indent=2))  
        assert response.status == 200

    def test03_verify_categories(self):
        response = request_context.get(chuck_api_url)
        categories = response.json()
        print(categories)
        print("Categories:")
        for category in categories:
            print("-", category)
        print(len(categories))
        assert len(categories) == 16, f"Expected 16 categories, got {len(categories)}"

    def test04_verify_who_has_more_jokes(self):
        api_params1 = {"query":"Barack Obama"}
        api_params2 = {"query":"Charlie Sheen"}
        barak_jokes = request_context.get(url="search",params=api_params1)
        charlie_jokes = request_context.get(url="search",params=api_params2)
        total_charlie_jokes = charlie_jokes.json()["total"]
        total_barak_jokes = barak_jokes.json()["total"]
        print(f"\nnumber of jokes for each one:")
        print(f"barack jokes:{total_barak_jokes}")
        print(f"charlie jokes:{total_charlie_jokes}")
        assert total_charlie_jokes > total_barak_jokes




        
        

       

        
       



           
        