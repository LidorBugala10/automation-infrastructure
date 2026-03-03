
from playwright.sync_api import Page
class GrafanaAdministrationPage:
    def __init__(self,page:Page):
        self.logo_grafana = page.locator("[class='css-1ul4bwd']")
        self.menu_items = page.locator("[class='css-v11ia6']")
        self.email_or_username_field = page.locator('[id=":r0:"]')
        self.user_name_filed = page.locator("[name='user']")
        self.password_filed = page.locator("[name='password']")
        self.submint_button = page.locator("[type='submit']")
        self.skip_button = page.locator("[class='css-1riaxdn']").nth(1)
        self.administration_button = page.locator("//p[text()='Administration']")
        self.Users_and_access_card = page.locator("[href='/admin/access']")
        
        #Users        
        self.users_card = page.locator("[href='/admin/users']")
        self.add_new_user_button = page.locator("[class='css-3l5qae-button']")


        #user createtion 
        self.name_filed = page.locator("[id^='name']")
        self.email_filed = page.locator("[id='email-input']")
        self.new_user_name_filed = page.locator("[id='username-input']")
        self.new_user_password_filed = page.locator("[id='password-input']")
        self.create_new_user_button = page.locator("[type='submit']")
        self.go_back_to_users_button = page.locator("[data-testid='data-testid Users breadcrumb']")
        self.admin_header = page.locator("//h1")
        self.rows_of_users = page.locator("[class='css-1e8ylo6-row']")
        self.rows_of_edit_users = page.locator("a[title='Edit user']")


        #deleting users
        self.edit_user_button = page.locator("[class='css-pu45w-button']").nth(0)
        self.delete_user_button = page.locator("//div/button[@class='css-sqsdvs-button']")
        self.delete_alert_button = page.locator("//div/button[@type='submit']")
        #searching users
        self.search_filed = page.locator("[class='css-r3ryyz-input-input']")

        #log_out
        self.admin_logo_button = page.locator("[alt='User avatar']")
        self.sign_out_button = page.locator("[href='/logout']")