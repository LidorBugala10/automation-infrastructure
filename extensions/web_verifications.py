from typing import List

from playwright.sync_api import Locator, expect
from smart_assertions import soft_assert, verify_expectations
import allure
from data.web.grafana_data import *

class WebVerify:
     

    


  
    @staticmethod    
    @allure.step("Verify that the element has text")
    def text(element: Locator,EXPECTED_HOME_HEADER,EXPECTED_ERORR_MESSAGE : str):
        
        """
        Verifies that the text of the element matches the expected text.
        """
        expect(element).to_have_text(EXPECTED_HOME_HEADER,EXPECTED_ERORR_MESSAGE)
        

    @staticmethod
    @allure.step("Verify String")
    def strings_are_equal(actual:str,expected:str,message=None):
        assert actual == expected,message


    @staticmethod
    @allure.step("Verify AI visual check succeeded")
    def strings_are_equal_bool(result: bool, expected_text: str, message: str = None):
        """
        Checks that the AI visual verification returned True.
        :param result: True/False from verify_with_vision
        :param expected_text: Text that היה אמור להימצא בתמונה
        :param message: Optional custom message
        """
        if not result:
            raise AssertionError(message or f"Expected text '{expected_text}' was not found in screenshot")






    @staticmethod
    @allure.step("Verify String")
    def string_contained(actual:str,expected:str,message=None):
        assert expected in actual

    @staticmethod
    @allure.step("Verify that the element is visible")
    def visible(element: Locator):
        """
        Verifies that the element is visible.
        """
        expect(element).to_be_visible()
    
    @staticmethod
    @allure.step("Verify that the element is not visible")
    def not_visible(element: Locator):
        """
        Verifies that the element is not visible.
        """
        expect(element).not_to_be_visible()
    
    @staticmethod
    @allure.step("Verifies that the number of elements matching the locator is equal to the expected count")
    def count(element: Locator, count: int):
        """
        Verifies that the number of elements matching the locator is equal to the expected count.
        """
        expect(element).to_have_count(count)


    @staticmethod
    @allure.step("Verifies that the number of elements matching the locator is equal to the expected count")
    def count_from_text(element: Locator, count: str):
        """
        Verifies that the number of elements matching the locator is equal to the expected count.
        """
        expect(element).to_have_count(int(count))

    @staticmethod
    @allure.step("Verify that the element contains the expected text")
    def contain_text(element: Locator, expected_text: str):
        """
        Verifies that the text of the element contains the expected text.
        """
        expect(element).to_contain_text(expected_text)
    
    @staticmethod
    @allure.step("Verify that the element has the expected value")
    def value(element: Locator, expected_value: str):
        """
        Verifies that the value of the element matches the expected value.
        """
        expect(element).to_have_value(expected_value)


    # Soft Assertions    
    @staticmethod
    @allure.step("Soft assertion to check if the element has the expected text")
    def soft_text(element: Locator, expected_text: str, message: str):
        """
        Soft assertion to check if the element has the expected text.
        Test execution will continue even if this assertion fails.
        """
        actual_text = element.inner_text()
        soft_assert(actual_text == expected_text, message)




    @staticmethod
    @allure.step("Verify that the actual value equals the expected value")
    def soft_values(actual:int,expected:int,message=None):
            soft_assert(actual==expected,message)



    @staticmethod
    @allure.step("Verify that keyword exists in list items")
    def soft_contain_in_list(keyword: str,list:List[str]):
        for item in list:
            soft_assert(keyword in item , f"{item} does not contain {keyword}")    

    @staticmethod
    @allure.step("Soft assertion to check if the element is visible")
    def soft_is_visible(element: Locator, message: str):
        """
        Soft assertion to check if the element is visible.
        Test execution will continue even if this assertion fails.
        """
        soft_assert(element.is_visible(), message)

    @staticmethod
    @allure.step("Raises all collected assertion errors at once")
    def soft_all():
        """Raises all collected assertion errors at once."""
        verify_expectations()



        