from pages.base_page import BasePage


class Dashboard(BasePage):
Scouts_Panel_xpath = "//*[text()=’Scouts Panel’]"
Scouts_Panel_xpath = "//*[@id=’__next’]/form/div/div[1]/h5"
Scouts_Panel_xpath = "//*[contains(@class, ‘MuiTypography-h5’)]"

Login_xpath= "//*[@id=’login’]"
Login_xpath= "//label[text()=’Login’]"
Login_xpath= "//*[@name = ‘login’ and @id = ‘login’]"


Password_xpath = "//*[@id=’password’]"
Password_xpath = "//label[text()=’Password’]"
Password_xpath = "//*[@name = ‘password’ and @id = ‘password’]"

Remind_password_xpath = "//*[@id=’__next’]/form/div/div[1]/a"
Remind_password_xpath = "//*[text()=’Remind password’]"
Remind_password_xpath = "//a[contains (@class, ‘MuiTypography’)]"

English_xpath = "//*[@role= ‘option’ and @tabindex=’0’]"
English_xpath = "//li[contains(@class, ‘MuiButtonBase-root’) and @data-value=’en’]"
English_xpath = "//li[contains(@role, ‘option’) and @data-value=’en’]"

Polski_xpath = "//div[contains(@class, ‘MuiSelect’)]"
Polski_xpath = "//div[contains(@role, ‘button’)]"
Polski_xpath = "//*[@role= ‘button’ and @tabindex=’0’]"

Zaloguj_xpath = "//*[text()=’Zaloguj’]"
Zaloguj_xpath = "//span[contains(@class, ‘MuiButton’)]"
Zaloguj_xpath = "//*[contains(@class, ‘MuiButton’) and text()=’Zaloguj’]"
pass

