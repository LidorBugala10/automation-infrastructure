import json
import pytest
from playwright.sync_api import Playwright
from smart_assertions import soft_assert,verify_expectations

WEATHER_API_URL="https://api.openweathermap.org/data/2.5/weather"
CITY_NAME="Jerusalem,IL"
API_KEY="ad48510a9aed1ff96b51557d94bc5964"
UNITS="metric"

class Test_Open_Weather_Map:
    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global request_context
        request_context=playwright.request.new_context(base_url=WEATHER_API_URL)
        yield
        request_context.dispose()

    def test_get_requset(self):
        api_paramas = {"appid":API_KEY,"q":CITY_NAME,"units":UNITS}
        response=request_context.get(url="",params=api_paramas)
        print("\n The Response is:")
        print(json.dumps(response.json(),indent=2))
        print(response.status)
        print(response.headers)
        print(response.headers["date"])
        soft_assert ("json" in response.headers["content-type"])
        soft_assert(response.status==200)
        verify_expectations()

        

        
   

        
