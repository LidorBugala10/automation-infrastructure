from playwright.sync_api import Page 
class WeatherPage:
    def __init__(self,page:Page):
        self.page = page
        self.city_field = page.locator("[name='q']").first
        self.search_result = page.locator("//b[1]/a").first
        self.humidty_element = page.locator("//span[text()='Humidity:']/..")

    
    def search_city(self,city):
        self.city_field.fill(city)
        self.page.keyboard.press("Enter")
        self.search_result.click()

    def get_humidity(self):
        humidity_from_web= int(self.humidty_element.inner_text().replace("Humidity:\n","").replace("%",""))
        print(f"\nHumidity from WEB:{humidity_from_web}")
        return humidity_from_web


        

