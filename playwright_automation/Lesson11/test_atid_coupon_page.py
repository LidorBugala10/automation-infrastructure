import allure 
from playwright.sync_api import Page
#actual_alert_message = []
class AtidCouponPage:
    def __init__(self,page:Page):
        self.page = page
        self.alert_message = None
        frame1 = page.frame_locator('[id="frame_a"]')
        self.Generate_Coupon_btn = page.locator('[id="button1"]')
        self.firat_name_field = frame1.locator('[id="first_name"]')
        self.last_name_field =frame1.locator('[id="last_name"]')
        self.coupon_field =  frame1.locator('[id="coupon"]')
        self.show_receipt_field = frame1.locator('[onclick="showAlert()"]')
        self.get_coupon = page.locator('[id="message-box"]')       

        
    def handle_alert(self, dialog):
        #actual_alert_message.append(dialog.message)
        print("\nAlert text is: " + dialog.message)
        self.alert_message=dialog.message
        dialog.accept()
       

    @allure.step("Fill and submit form with coupon")
    def fiil_and_submit_with_coupon(self,first_name,last_name):
        self.Generate_Coupon_btn.click()
        self.firat_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        coupon = self.coupon_field.fill(self.get_coupon.inner_text().replace("Your coupon code is: " ,""))
        self.page.once("dialog", lambda dialog: self.handle_alert(dialog)) 
        self.show_receipt_field.click()

    def get_alert_message(self):
        return self.alert_message





    


        