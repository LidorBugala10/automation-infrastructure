from playwright.sync_api import Page
import allure
class FunKidsLive:
    def __init__(self, page:Page):
        self.page = page
        self.fish_facts = page.locator('[class="wp-block-heading"]')

    def print_facts(self):
        facts = self.fish_facts.all()
        print("\nFacts:")
        for fact in facts:
            print(fact.inner_text())


    def get_total_facts(self):
        total_facts = len(self.fish_facts.all())
        print(f"\nThe total facts is:{total_facts}") 
        return total_facts       