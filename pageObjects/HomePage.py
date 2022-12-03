import time

from selenium.webdriver.common.by import By


class HomePage:
    text_username_name = 'username'
    text_password_name = 'password'
    btn_login_xpath ="//button[@type='submit']"
    linkText_forgotPass_xpath="//p[text()='Forgot your password? ']"
    btn_resetPassword_xpath="//button[@type='submit']"
    text_passwordResetMessage_xpath="//h6[contains(@class,'orangehrm-forgot-password-title')]"
    header_dasboard_xpath="//h6[contains(@class,'topbar-header-breadcrumb-module')]"

    def __init__(self, driver):
        self.driver = driver


    def enterUserName(self):
        self.driver.find_element(By.NAME,self.text_username_name).clear()
        self.driver.find_element(By.NAME, self.text_username_name).send_keys('Admin')

    def enterPassword(self):
        self.driver.find_element(By.NAME,self.text_password_name).clear()
        self.driver.find_element(By.NAME, self.text_password_name).send_keys('admin123')

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def clickForgotPassword(self):
        self.driver.find_element(By.XPATH,self.linkText_forgotPass_xpath).click()

    def resetPassword(self):
        self.driver.find_element(By.XPATH,self.btn_resetPassword_xpath).click()
        time.sleep(3)
        try:
            return self.driver.find_element(By.XPATH,self.text_passwordResetMessage_xpath).text
        except:
            None

    def checkHeader(self):
        try:
            self.driver.find_element(By.XPATH,self.header_dasboard_xpath).is_displayed()
            print('************************************************************************************')
        except:
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            return False