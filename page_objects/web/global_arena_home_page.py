from playwright.sync_api import Page
class GlobalArenaHomePage:
    def __init__(self,page:Page):
        self.home_page_title = page.locator("//h1").nth(0)
        self.browse_all_tickets_button = page.locator("//button[text()='Browse All Tickets']")
        self.add_ticket_button = page.locator('[onclick="addToCart(3)"]').nth(1)
        self.add_another_ticket_button = page.locator('[onclick="addToCart(2)"]').nth(1)
        self.add_additional_ticket_button = page.locator('[onclick="addToCart(1)"]').nth(1)
        self.cart_item = page.locator('[class="cart-icon"]')
        self.remove_first_match_ticket_button = page.locator('[onclick="removeFromCart(1)"]')
        self.remove_second_match_ticket_button = page.locator('[onclick="removeFromCart(2)"]')
        self.remove_third_match_ticket_button = page.locator('[onclick="removeFromCart(3)"]')
        self.empty_cart_message = page.locator("//p[text()='Your cart is empty.']")
        self.my_order = page.locator('//*[@id="auth-links"]/a[1]')
        self.logo_item = page.locator('[class="logo"]').first

        self.all_tickets_from_home_page = page.locator('[class="card-price"]')
        self.name_of_all_tickets = page.locator('[class="card-title"]')
        self.all_tickets_text = page.locator('[id="catalog-title"]')      
        

