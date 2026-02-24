from playwright.sync_api import Page
import allure
class DragonBallWeb:
    def __init__(self, page:Page):
        self.page = page
        self.items = page.locator("//h2[contains(@class,'MuiTypography-h2')]")
        self.scroll_element = page.locator("//*[text()='Scroll Down for more characters']")

    @allure.title("verify scroll to buttom")
    @allure.description("This test verify scroll to buttom")
    def scroll_to_buttom(self):
        while(self.scroll_element.is_visible()):
            self.page.keyboard.down("PageDown")

    @allure.title("Verify scroll to bottom and print characters")
    @allure.description("This function scrolls to the bottom and logs all characters found on the page.")   
    def print_characters(self):
        print("\n") 
        for i,item in enumerate(self.items.all()):
            print(f"{i+1} - {item.inner_text()}")    

    @allure.title("Verify scroll to bottom and print characters")
    @allure.description("This function counts all characters found on the page after scrolling to the bottom.")
    def get_characters_count(self):
        return self.items.count()
        

        