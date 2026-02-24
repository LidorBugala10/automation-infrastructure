import json
import pytest
from playwright.sync_api import Playwright


STUDENT_API_URL = "http://localhost:9000/student/"
HEADERS = {'Content-type':'application/json'}
STUDENT_ID = '50'
class TestStudentsAPI:

    @pytest.fixture(scope="class",autouse=True)
    def setup_playwright_context(self,playwright:Playwright):
        global request_context
        request_context = (playwright.request.new_context(base_url=STUDENT_API_URL,extra_http_headers=HEADERS))
    def teardown_class(cls):
        request_context.dispose()     
    

    def test01_verify_get_request(self): 
        response = request_context.get(url="list")
        students = response.json()
        print(json.dumps(students,indent=2))
        print("STATUS",response.status)
        assert response.status == 200
        
        
    def test02_verify_post_request(self):
        student_data = {'firstName':'lidor','lastName':'bugala','email':'bugala66@gmail.com','programme':'QA',"courses":["QA"]}
        response = request_context.post(STUDENT_API_URL,data=student_data)
        response_json = response.json()
        print(response_json)
        print("STATUS", response.status)
        assert response.status == 201

    def test03_verify_put_request(self):
        updated_student_data = {'firstName':'Lidor','lastName':'bugala','email':'bugala96@gmail.com','programme':'Physics'}
        response = request_context.put(url="109",data=updated_student_data)
        response_json = response.json()
        print(response_json)
        print("STATUS", response.status)
        assert response.status == 200

    def test04_verify_delete_request(self):
        response = request_context.delete("101") 
        print(response.json)
        assert response.status == 204  

           


        

        