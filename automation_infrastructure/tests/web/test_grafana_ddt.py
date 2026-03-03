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
        home_flows.searc_for_user(new_user_data["name"])
        # WebVerify.soft_count(web_flow.grafana_administration_page.rows_of_users,EXPECTED_RESULT,"Users table count mismatch")
        # WebVerify.soft_all()
    
