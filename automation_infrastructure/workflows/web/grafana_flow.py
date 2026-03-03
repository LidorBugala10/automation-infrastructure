
from playwright.sync_api import Page
from data.api.grafana_api_data import *
from extensions.ui_actions import UIActions
from page_objects.web.grafana_home_page import GrafanaHomePage
from page_objects.web.grafana_login_page import GrafanaLoginPage
from page_objects.web.grafana_administration_page import GrafanaAdministrationPage




class GrafanaFlow:
    def __init__(self,page:Page):
        self.page = page
        self.grafana_login_page = GrafanaLoginPage(page)
        self.grafana_home_page = GrafanaHomePage(page)
        self.grafana_administration_page = GrafanaAdministrationPage(page)
        
    def sign_in(self,user_name,password)->None:
        UIActions.update_text(self.grafana_login_page.search_field,user_name)
        UIActions.update_text(self.grafana_login_page.password_field,password)
        UIActions.click(self.grafana_login_page.login_button)
    
    def skip_change_password(self):
        UIActions.click(self.grafana_login_page.skip_button)
   
    # def is_signed_in(self)->bool:
    #     return "login" in self.page.url

    def get_home_header(self):
        home_header = UIActions.get_text(self.grafana_home_page.home_header)
        print(f"\nHome Header: {home_header}")
        return home_header
    



    def get_error_massage(self):    
       error_massage = UIActions.get_text(self.grafana_login_page.error_massage)
       print(f"\nThe error message is:{error_massage}")
       return error_massage 
    



    def create_new_team(self,name_of_team,email):
       UIActions.click(self.grafana_home_page.admin_menu_item)
       UIActions.click(self.grafana_home_page.users_and_access_tab)
       UIActions.click(self.grafana_home_page.users_and_access_toggle)
       UIActions.click(self.grafana_home_page.teams_menu_item)
       UIActions.click(self.grafana_home_page.new_team_button)
       UIActions.update_text(self.grafana_home_page.team_name_input,name_of_team)
       UIActions.update_text(self.grafana_home_page.team_email_input,email)
       UIActions.click(self.grafana_home_page.create_team_button)
       UIActions.click(self.grafana_home_page.teams_breadcrumb)

    def get_name_of_team(self):
        name_of_team = UIActions.get_text(self.grafana_home_page.team_name_label)
        print(f"\nThe name of the team is :{name_of_team}")
        return name_of_team
    
    def delete_team(self,name_of_team,email):
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

    def get_text_of_deleted_team(self):
        text_after_delete = UIActions.get_text(self.grafana_home_page.team_deleted_message)
        print(f"\nThe massage after deleting the team is :{text_after_delete}")
        return text_after_delete
    
    def click_on_search_item(self,name_of_item):
        UIActions.click(self.grafana_home_page.search_input)
        UIActions.update_text(self.grafana_home_page.quick_search_input ,name_of_item)
        UIActions.click(self.grafana_home_page.search_result_item)
        UIActions.click(self.grafana_home_page.profiles_menu_item)
    
    def get_home_header_profiles(self):
        text_of_profiles = UIActions.get_text(self.grafana_home_page.profiles_header)
        print(f"\nThe text is :{text_of_profiles}")
        return text_of_profiles
    
    def search_item_with_invalid_name(self,invalid_name):
        UIActions.click(self.grafana_home_page.search_input )
        UIActions.update_text(self.grafana_home_page.quick_search_input,invalid_name)

    def get_search_massage(self):
        search_maasage = UIActions.get_text(self.grafana_home_page.no_results_message)
        print(f"\nThe text is :{search_maasage}")
        return search_maasage    


    def verify_login(self,user_name,password):
        UIActions.update_text(self.grafana_administration_page.user_name_filed,user_name)
        UIActions.update_text(self.grafana_administration_page.password_filed,password)
        UIActions.click(self.grafana_administration_page.submint_button)
        UIActions.click(self.grafana_administration_page.skip_button)

    def navigate_to_users(self):
        # UIActions.click(self.grafana_administration_page.logo_grafana)
        #entering to the creating new user page 
        UIActions.click(self.grafana_administration_page.administration_button)
        UIActions.click(self.grafana_administration_page.Users_and_access_card)
        UIActions.click(self.grafana_administration_page.users_card)
        # UIActions.click(self.grafana_administration_page.add_new_user_button)


    def register_new_user(self,name,email,username,user_password):
        #fiiling filed 
        UIActions.click(self.grafana_administration_page.add_new_user_button)

        UIActions.update_text(self.grafana_administration_page.name_filed,name)
        UIActions.update_text(self.grafana_administration_page.email_filed,email)
        UIActions.update_text(self.grafana_administration_page.new_user_name_filed,username)
        UIActions.update_text(self.grafana_administration_page.new_user_password_filed,user_password)
        UIActions.click(self.grafana_administration_page.create_new_user_button)
        UIActions.click(self.grafana_administration_page.go_back_to_users_button)
        
    def searc_for_user(self,username):
        UIActions.update_text(self.grafana_administration_page.search_filed,username)


    def delete_all_users_except_admin(self):
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

    def log_out_form_garfana(self):
        UIActions.click(self.grafana_administration_page.admin_logo_button)
        UIActions.click(self.grafana_administration_page.sign_out_button)
    



        

       