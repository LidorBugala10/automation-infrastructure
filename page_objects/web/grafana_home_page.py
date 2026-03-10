from playwright.sync_api import Page
class GrafanaHomePage:
    def __init__(self,page:Page):
        self.home_page_header = page.locator("[class='css-1ti7uft']")
        self.admin_menu_item  = page.locator("//p[text()='Administration']")
        self.users_and_access_tab = page.locator ('[class="css-14ffdzi"]').nth(2) 
        self.users_and_access_toggle  = page.locator("button[aria-label*='Users and access']")
        self.teams_menu_item = page.locator("//p[text()='Teams']")
        self.new_team_button = page.locator("//span[text()='New Team']")
        self.team_name_input = page.locator('[id="team-name"]')
        self.team_email_input = page.locator('[id="team-email"]')
        self.create_team_button= page.locator('[class="css-1riaxdn"]').nth(1)
        self.teams_breadcrumb = page.locator('[data-testid="data-testid Teams breadcrumb"]')
        #נתיב ניווט של הצוותים

        self.team_name_label = page.locator('[class="css-6i6vus"]')
        self.remove_team_button = page.locator('[class="css-bb0rlp"]').nth(0)
        self.confirm_delete_team_button = page.locator("//span[text()='Delete']").nth(0)
        self.search_team_field = page.locator('[type="text"]')
        self.team_deleted_message = page.locator("//span[text()='No teams found']")
        self.search_input  = page.locator('[class="css-1vpmr4y-input-input"]')
        self.quick_search_input = page.locator('[class="css-150s1rd-kbar-search-input"]')
        self.search_result_item = page.locator('[class="css-5mekwu"]')
        self.profiles_menu_item = page.locator("//a[text()='Profiles']")
        self.profiles_header = page.locator('[class="css-i1ei61"]')
        self.no_results_message = page.locator('[class="css-ciuvi3"]')





























