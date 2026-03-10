import json
import allure
from playwright.sync_api import APIRequestContext
import pytest
from data.api.grafana_api_data import *
from extensions.api_actions import APIActions
class GrafanaApiFlows:
    def __init__(self,request_context:APIRequestContext):
        self.api =  APIActions(request_context)
    
    @allure.step("GET - Retrieve all users")
    def get_users(self):
        response = self.api.get(url="/api/org/users")
        return response
    
    @allure.step("GET - Retrieve teams by name")
    def get_teams(self):
        response = self.api.get(url=F"api/teams/search?name={GRAFANA_TEAMS_API}")
        print(json.dumps(response.json(),indent=3))
        return response


    @allure.step("POST - Create user by Name, Email,password and login")
    def create_user(self,name:str,email:str,login:str,password:str):
        user_data = {
            "name":name,
            "email":email,
            "login":login,
            "password":password,
              }
        response_data = self.api.post(url="/api/admin/users",payload=user_data)
        return response_data
    
    @allure.step("POST - Create team by Name and Email")
    def create_team(self,name:str,email:str):
        user_data = { "name":name,
                       "email":email 

        }
        response_data = self.api.post(url="api/teams",payload=user_data)
        return response_data
    

    @allure.step("DELETE - Delete team by Team ID")
    def delete_team(self,team_id:str):
        user_data = {"id": id}
        response_data = self.api.delete(url=f"api/teams/{team_id}")
        return response_data
    
    @allure.step("DELETE - Delete user by User ID")
    def delete_user(self, user_id:int):
        response = self.api.get(url="/api/org/users")
        users = response.json()
        print(users)
        user_to_delete = None
        for user in users:
            if user["userId"] == user_id:
                user_to_delete = user
                break
        if not user_to_delete:
            pytest.fail(f"User with ID {user_id} not found")
        if user_to_delete["login"].lower() == "admin":
            pytest.fail("cannot delete admin user")
        delete_response = self.api.delete(url=f"/api/org/users/{user_id}")
        return delete_response
            


    @allure.step("PUT - Update team by Name and Email")
    def put_team(self,name:str,email:str):
        team_data = { "name":name,
                       "email":email 

        }
        response_data = self.api.put(url=F"api/teams/{TEAM_ID}",payload=team_data)
        return response_data
    
    @allure.step("PUT - Update user by Name,Email and login ")
    def put_user(self,name:str,email:str,login:str):
        user_data = {"name": name,
        "email": email,
        "login": login
        }
        response = self.api.put(url=f"/api/users/{PUT_USER_ID}",payload=user_data)
        return response
    

    @allure.step("POST - Create duplicate user attempt by Login,Name,Email and Password")
    def post_duplicate_user(self,name:str,email:str,login:str,password:str):
        user_data = {"name":name,
            "email":email,
            "login":login,
            "password":password,

        }
        response_data = self.api.post(url="/api/admin/users",payload=user_data)
        return response_data
    
    
    @allure.step("POST - Add member to team by User ID ")
    def post_member(self,user_id:int):
        member_data = { "userId":user_id

        }
        response_data = self.api.post(url=F"api/teams/{TEAM_ID}/members",payload=member_data)
        return response_data
    
  
    

