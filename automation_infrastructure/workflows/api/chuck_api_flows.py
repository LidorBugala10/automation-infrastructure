from playwright.sync_api import APIRequestContext, APIResponse
from data.api.grafana_api_data import *
from extensions.api_actions import APIActions

class ChuckApiFlows:

    def __init__(self,request_context:APIRequestContext):
        self.api = APIActions(request_context)

    def test01(self)->APIActions:
        respone = self.api.get(GRAFANA_BASE_URL)
        print("Status Code:", respone.status_code)
        print("Response JSON:", respone.json()) 
        # for user in users:
        #     print(f"User: {user['login']} | Email: {user['email']}")   







       # def search_for_joke(self,query:str)->APIResponse:
    #     params = {"query":query}
    #     return self.api.get(FREE_SEARCH_RESOURCE,params)
 

    # def get_all_user(self):
    #     response = self.api.get("api/admin/users")
    #     print(response.json())     


