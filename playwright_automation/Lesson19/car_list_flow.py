from typing import List
from playwright.sync_api import Page
from playwright_automation.Lesson19.car_list_page import CarListPage

class CarFlows:
    def __init__(self,page:Page):
        self.page = page
        self.cars = CarListPage(page)

    def move_all_cars_to_selected_cars(self)->None:
        available_cars = self.cars.available_cars.all()
        for _ in range(len(available_cars)):
            available_cars[0].click()
    
    def get_total_selected_cars(self)->int:
        return self.cars.selected_cars.count()
    
    def get_total_available_cars(self)->int:
        return self.cars.available_cars.count()
    

    def get_available_cars_list(self)->List[str]:
        return self.cars.available_cars.all_inner_texts()
    
    
    def get_selected_cars_list(self)->List[str]:
        return self.cars.selected_cars.all_inner_texts()
        
    
    def is_all_contained(self,cars_list:List[str])->bool:
        selected_cars = self.get_selected_cars_list()
        all_contained = True
        for available in cars_list:
            if available not in selected_cars:
                all_contained = False
                break
        return all_contained




