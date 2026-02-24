import json
import pytest
from playwright.sync_api import Playwright,Page
import requests
from smart_assertions import soft_assert,verify_expectations
import requests

dragon_ball_url = "https://dragonball-api.com/api/characters"

class Test_Api_dragon_ball_Website:
    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global request_context,page 
        request_context=playwright.request.new_context(base_url=dragon_ball_url)
        yield
        request_context.dispose()

    def test01_verify_(self,page:Page):
        response = requests.get(dragon_ball_url) 
        data = response.json()
        for i in range(len(data["items"])):
            print(data["items"][i]["name"])
        assert response.status_code==200
    

        
    
