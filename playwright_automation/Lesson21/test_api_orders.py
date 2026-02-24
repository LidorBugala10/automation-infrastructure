import json
import pytest
from playwright.sync_api import Playwright,Page
import requests
from smart_assertions import soft_assert,verify_expectations
import requests

order_url = "http://localhost:3000/orders"

class Test_Api_dragon_ball_Website:
    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global request_context,page 
        request_context=playwright.request.new_context(base_url=order_url)
        yield
        request_context.dispose()

    def test01_verify_order(self,page:Page):
        response = requests.get(order_url) 
        orders = response.json()
        print(json.dumps(orders,indent=2))
        for order in orders:
            total = 0
            for i in range(len(order["orderItems"])):
                #print(order["orderItems"][i]["details"]["price"])
                total += order["orderItems"][i]["details"]["price"]
            print(f"total amount is : {total}")
            expected_amount = order["totalAmount"]
            print(f"expected_amount: {expected_amount}")
            soft_assert (total==expected_amount)
        verify_expectations()
            

               
            

        
        
        


     
        

        