
import types
import allure
from google import genai
from google.genai import types as genai_types
from playwright.sync_api import Page
from data.api.grafana_api_data import *
from extensions.ui_actions import UIActions
from page_objects.web.grafana_home_page import GrafanaHomePage
from page_objects.web.grafana_login_page import GrafanaLoginPage
from page_objects.web.grafana_administration_page import GrafanaAdministrationPage
from page_objects.web.grafana_plugins_page import GrafanaPluginsPage




class GrafanaFlow:
    def __init__(self,page:Page):
        self.page = page
        self.grafana_login_page = GrafanaLoginPage(page)
        self.grafana_home_page = GrafanaHomePage(page)
        self.grafana_administration_page = GrafanaAdministrationPage(page)
        self.grafana_plugins_page = GrafanaPluginsPage(page)

    @allure.step("Navigate to plugins page and search for application")
    def google_products(self,app_name):
        UIActions.click(self.grafana_plugins_page.administration_button)
        UIActions.click(self.grafana_plugins_page.plugins_and_data_button)
        UIActions.click(self.grafana_plugins_page.plugins_button)
        UIActions.update_text(self.grafana_plugins_page.plugins_search_field,app_name)

    @allure.step("Get all Google applications names from plugins list")
    def get_all_google_app(self):
        google_apps = self.grafana_plugins_page.google_apps.all()
        apps_names = []
        for app in google_apps:
            name = app.inner_text()
            print(f"The name of app is: {name}")
            apps_names.append(name)
        return apps_names
    
    @allure.step("Get the amount of Google applications displayed")
    def get_products_amount(self):
        google_apps = self.grafana_plugins_page.google_apps.all()
        return len(google_apps)

    @allure.step("Verify using AI vision that the page contains home header")
    def verify_with_vision(self, EXPECTED_HOME_HEADER: str) -> bool:
        client = genai.Client(api_key=GEMENI_API_KEY)
        screenshot_bytes = self.page.screenshot(type="png")
        with open("last_screenshot.png", "wb") as f:
            f.write(screenshot_bytes)
            print("Screenshot saved as last_screenshot.png")
        prompt = (
           f"Examine the screenshot. Does it contain the text '{EXPECTED_HOME_HEADER}'? Respond with 'Yes' or 'No'."
        )
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                prompt,
                genai_types.Part.from_bytes(
                    data=screenshot_bytes,
                    mime_type="image/png"
                )
            ]
        )
        result = response.text.strip().lower()
        print("AI says:", result)
        return "yes" in result


    @allure.step("Sign in with username and paasword")   
    def sign_in(self,user_name,password) -> None:
        UIActions.update_text(self.grafana_login_page.search_field,user_name)
        UIActions.update_text(self.grafana_login_page.password_field,password)
        UIActions.click(self.grafana_login_page.login_button)
    

    @allure.step("Skip password change screen")
    def skip_change_password(self) -> None:
        UIActions.click(self.grafana_login_page.skip_button)
   
    @allure.step("Get home page header")
    def get_home_page_header(self) -> str:
        home_page_header = UIActions.get_text(self.grafana_home_page.home_page_header)
        print(f"\nHome page Header: {home_page_header}")
        return home_page_header
    

    @allure.step("Get login error message")
    def get_error_massage(self) -> str:    
       error_massage = UIActions.get_text(self.grafana_login_page.error_massage)
       print(f"\nThe error message is:{error_massage}")
       return error_massage 
    


    @allure.step("Create new team by name and email")
    def create_new_team(self, name_of_team, email) -> None:
       UIActions.click(self.grafana_home_page.admin_menu_item)
       UIActions.click(self.grafana_home_page.users_and_access_tab)
       UIActions.click(self.grafana_home_page.users_and_access_toggle)
       UIActions.click(self.grafana_home_page.teams_menu_item)
       UIActions.click(self.grafana_home_page.new_team_button)
       UIActions.update_text(self.grafana_home_page.team_name_input,name_of_team)
       UIActions.update_text(self.grafana_home_page.team_email_input,email)
       UIActions.click(self.grafana_home_page.create_team_button)
       UIActions.click(self.grafana_home_page.teams_breadcrumb)



    @allure.step("Get created team name")
    def get_name_of_team(self) -> str:
        name_of_team = UIActions.get_text(self.grafana_home_page.team_name_label)
        print(f"\nThe name of the team is :{name_of_team}")
        return name_of_team
    

    @allure.step("Delete team by name and email")
    def delete_team(self, name_of_team, email) -> None:
        UIActions.click(self.grafana_home_page.admin_menu_item)
        UIActions.click(self.grafana_home_page.users_and_access_tab)
        UIActions.click(self.grafana_home_page.users_and_access_toggle)
        UIActions.click(self.grafana_home_page.teams_menu_item)
        UIActions.click(self.grafana_home_page.new_team_button )
        UIActions.update_text(self.grafana_home_page.team_name_input,name_of_team)
        UIActions.update_text(self.grafana_home_page.team_email_input,email)
        UIActions.click(self.grafana_home_page.create_team_button)
        UIActions.click(self.grafana_home_page.teams_breadcrumb)
        UIActions.click(self.grafana_home_page.remove_team_button)
        UIActions.click(self.grafana_home_page.confirm_delete_team_button)
        UIActions.update_text(self.grafana_home_page.search_team_field,name_of_team)



    @allure.step("Get confirmation message after team deletion")
    def get_text_of_deleted_team(self) -> str:
        text_after_delete = UIActions.get_text(self.grafana_home_page.team_deleted_message)
        print(f"\nThe massage after deleting the team is :{text_after_delete}")
        return text_after_delete
    

    @allure.step("Search for item by name")
    def click_on_search_item(self, name_of_item) -> None:
        UIActions.click(self.grafana_home_page.search_input)
        UIActions.update_text(self.grafana_home_page.quick_search_input ,name_of_item)
        UIActions.click(self.grafana_home_page.search_result_item)
        UIActions.click(self.grafana_home_page.profiles_menu_item)
    

    @allure.step("Get profiles header")
    def get_home_header_profiles(self) -> str:
        text_of_profiles = UIActions.get_text(self.grafana_home_page.profiles_header)
        print(f"\nThe text is :{text_of_profiles}")
        return text_of_profiles
    


    @allure.step("Search with invalid name")
    def search_item_with_invalid_name(self, invalid_name) -> None:
        UIActions.click(self.grafana_home_page.search_input )
        UIActions.update_text(self.grafana_home_page.quick_search_input,invalid_name)


    @allure.step("Get no-results message")
    def get_search_massage(self) -> str:
        search_maasage = UIActions.get_text(self.grafana_home_page.no_results_message)
        print(f"\nThe text is :{search_maasage}")
        return search_maasage    


    @allure.step("Verify login with username and password")
    def verify_login(self, user_name, password) -> None:
        UIActions.update_text(self.grafana_administration_page.user_name_filed,user_name)
        UIActions.update_text(self.grafana_administration_page.password_filed,password)
        UIActions.click(self.grafana_administration_page.submint_button)
        UIActions.click(self.grafana_administration_page.skip_button)


    @allure.step("Navigate to users page")
    def navigate_to_users(self) -> None:
        UIActions.click(self.grafana_administration_page.administration_button)
        UIActions.click(self.grafana_administration_page.Users_and_access_card)
        UIActions.click(self.grafana_administration_page.users_card)


    @allure.step("Register new user by username ,email ,password and name" )
    def register_new_user(self, name, email, username, user_password) -> None:
        UIActions.click(self.grafana_administration_page.add_new_user_button)
        UIActions.update_text(self.grafana_administration_page.name_filed,name)
        UIActions.update_text(self.grafana_administration_page.email_filed,email)
        UIActions.update_text(self.grafana_administration_page.new_user_name_filed,username)
        UIActions.update_text(self.grafana_administration_page.new_user_password_filed,user_password)
        UIActions.click(self.grafana_administration_page.create_new_user_button)
        UIActions.click(self.grafana_administration_page.go_back_to_users_button)
        

    @allure.step("Search for user by user name")
    def search_for_user(self, user_name) -> None:
        UIActions.update_text(self.grafana_administration_page.search_filed,user_name)


    @allure.step("Delete all users except admin user")
    def delete_all_users_except_admin(self) -> None:
            position = 0
            count = self.grafana_administration_page.rows_of_users.count()
            users = self.grafana_administration_page.rows_of_edit_users.all()
            while(count>1):
                if UIActions.get_text(users[position]) == ADMIN_USER:
                    position+=1
                else:
                    UIActions.click(users[position])
                    UIActions.click(self.grafana_administration_page.delete_user_button)
                    UIActions.click(self.grafana_administration_page.delete_alert_button)
                users = self.grafana_administration_page.rows_of_edit_users.all()
                count = self.grafana_administration_page.rows_of_users.count()

    @allure.step("Logout from Grafana")
    def log_out_form_garfana(self) -> None:
        UIActions.click(self.grafana_administration_page.admin_logo_button)
        UIActions.click(self.grafana_administration_page.sign_out_button)


    def is_signed_in(self)->bool:
        return  not ("login" in self.page.url)
    



        

       