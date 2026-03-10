import pytest

from extensions.web_verifications import WebVerify
from utils.common_ops import load_config, read_data_from_csv
from workflows.web.grafana_flow import GrafanaFlow

config = load_config()
USERS_CSV = config["USERS_CSV_PATH"]
class TestGrafanaDDT:
    
    @pytest.mark.parametrize("new_user_data",read_data_from_csv(USERS_CSV))
    def test_verify_new_user(self,home_flows:GrafanaFlow,new_user_data):
        home_flows.navigate_to_users()
        home_flows.register_new_user(new_user_data["name"],new_user_data["email"],new_user_data["username"],new_user_data["user_password"])
        home_flows.search_for_user(new_user_data["name"])
        WebVerify.count_from_text(home_flows.grafana_administration_page.rows_of_users,new_user_data["expected_users"])
    
