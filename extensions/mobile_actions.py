
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class MobileActions:

    @staticmethod
    @allure.step("Click on element")
    def click(driver, locator, timeout=10):

        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        element.click()

    DEFAULT_TIMEOUT = 10

    @allure.step("Type text into element")
# שנה את הסדר כאן: קודם text ואז timeout
    def type_text(driver, locator, text, timeout=DEFAULT_TIMEOUT):
        timeout = float(timeout) 
        
        # שינוי חשוב: visibility_of_element_located מצפה ל-Tuple אחד, לא שני ארגומנטים
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(text)

    @staticmethod
    @allure.step("Get text from element")
    def get_text(driver, locator, timeout=DEFAULT_TIMEOUT):
        timeout = float(timeout)
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        
        # באנדרואיד, נסה קודם את ה-Attribute שנקרא "text"
        text = element.get_attribute("text")
        
        # אם זה לא עובד (למשל ב-iOS או רכיבים אחרים), נחזור לשיטה הרגילה
        if text is None or text == "":
            text = element.text
            
        return text.strip() if text else ""