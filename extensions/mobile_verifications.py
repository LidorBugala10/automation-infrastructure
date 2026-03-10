import allure
class MobileVerifications:

    @staticmethod
    @allure.step("Verify String")
    def strings_are_equal(actual:str,expected:str,message=None):
        assert actual == expected,message

    @staticmethod
    @allure.step("Verify number of elements")
    def list_size(elements_list, expected_size: int, message="List size mismatch"):
        # elements_list הוא התוצאה של driver.find_elements
        actual_size = len(elements_list)
        assert actual_size == expected_size, f"{message}. Expected: {expected_size}, Actual: {actual_size}"