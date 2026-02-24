import pytest
from playwright.sync_api import Playwright

from playwright_automation.Lesson15.weather_page import WeatherPage


class TestOpenWeatherUIAndAPI:

    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global browser,context,page,request_context,weather_page    
        #WEB INIT
        browser = playwright.chromium.launch(headless= False,channel="chrome",slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()      
        page.goto("https://old.openweathermap.org/")
        weather_page = WeatherPage(page)
        #API INIT
        request_context = playwright.request.new_context(base_url="https://api.openweathermap.org/")
        yield
        #API TEARDOWN
        request_context.dispose()
        #WEB TEARDWON
        context.close()
        page.close()

    def test01_verify_humidity_from_web_and_api(self):
        #WEB
        weather_page.search_city("jerusalem")
        humidity_from_web= weather_page.get_humidity()

        #API
        api_params = {"appid":"ad48510a9aed1ff96b51557d94bc5964","units":"metric","q":"jerusalem"}
        response = request_context.get(url="data/2.5/weather",params=api_params)
        weather_data = response.json()
        huimdity_from_api = weather_data["main"]["humidity"]
        print(f"\nHumidity from API:{huimdity_from_api}")

        #Verification
        assert humidity_from_web == huimdity_from_api

       

        


        
           

    
    