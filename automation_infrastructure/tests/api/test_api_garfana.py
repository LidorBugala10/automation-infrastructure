import json

import pytest
from playwright.sync_api import Playwright, sync_playwright

from data.api.grafana_api_data import*
from extensions.api_verifications import APIVerify
from workflows.api.grafana_api_flows import GrafanaApiFlows


class TestGrafanaAPI:

    def test_get_users(self, grafana_api_flows:GrafanaApiFlows):
        print(grafana_api_flows.get_users())
        APIVerify.status_code(grafana_api_flows.get_users(),EXPECTED_STATUS_SUCCESS_CODE)

    def test_post_users(self,grafana_api_flows:GrafanaApiFlows):
        response = grafana_api_flows.create_user(NAME,EMAIL,LOGIN,PASSWORD)
        APIVerify.status_code(response,EXPECTED_USER_CREATED_CODE)

    def test_get_teams(self,grafana_api_flows:GrafanaApiFlows):
        print(grafana_api_flows.get_teams())
        APIVerify.status_code(grafana_api_flows.get_teams(),EXPECTED_STATUS_SUCCESS_CODE)

    def test_post_teams(self,grafana_api_flows:GrafanaApiFlows):
        response = grafana_api_flows.create_team(TEAM_NAME,EMAIL_TEAM)
        APIVerify.json_value_equals(grafana_api_flows.api.extract_json(response),MESSAGE_KEY,EXPECTED_MESSAGE_VALUE) 

    def test_delete_team(self,grafana_api_flows:GrafanaApiFlows):
       response = grafana_api_flows.delete_team(TEAM_ID)
       print(response)
       APIVerify.json_value_equals(grafana_api_flows.api.extract_json(response),DELETED_MESSAGE_KEY,EXPECTED_MESSAGE_DELETE)

    def test_put_team(self,grafana_api_flows:GrafanaApiFlows):
        response = grafana_api_flows.put_team(UPDATE_NAME,UPDATE_EMAIL)
        print(response)
        APIVerify.json_value_equals(grafana_api_flows.api.extract_json(response),UPDATE_MESSAGE_KEY,EXPECTED_UPDATE_MESSAGE)

    def test_post_member(self,grafana_api_flows:GrafanaApiFlows):
        response = grafana_api_flows.post_member(USER_ID)
        print(response)
        APIVerify.status_code(response,EXPECTED_STATUS_SUCCESS_CODE) 

    def test_put_user(self,grafana_api_flows:GrafanaApiFlows):
        response = grafana_api_flows.put_user(PUT_USER_NAME,PUT_USER_EMAIL,PUT_USER_LOGIN)  
        print(response)
        APIVerify.status_code(response,EXPECTED_STATUS_SUCCESS_CODE)   

    def test_post_duplicate_user(self,grafana_api_flows:GrafanaApiFlows):
        response = grafana_api_flows.post_duplicate_user(USER_1["NAME"],USER_1["EMAIL"],USER_1["LOGIN"],USER_1["PASSWORD"])
        response_after_create = grafana_api_flows.post_duplicate_user(USER_1["NAME"],USER_1["EMAIL"],USER_1["LOGIN"],USER_1["PASSWORD"])
        print(response_after_create)
        print(response)
        APIVerify.status_text_contains(response_after_create,RESPONSE_MESSAGE_AFTER_CREATE)

    def test_delete_user(self,grafana_api_flows:GrafanaApiFlows):
        response = grafana_api_flows.delete_user(USER_ID)
        print(response)
        APIVerify.status_code(response,EXPECTED_STATUS_SUCCESS_CODE)         


        
        
    


        




            
