 from pages.base_page import BasePage


 class LoginPage(BasePage):
     scouts_panel_xpath = "//*[text()="Scouts Panel"]"
     login_xpath= "//*[@id="login"]"
     password_xpath = "//*[@id="password"]"

     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)