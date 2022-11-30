import time
from pageObjects.HomePage import HomePage # importing the UI elements of OrangeHrm homepage
import os

class Test_001_adminLogin:
    baseURL= 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    def test_login(self,setup): # setup method is present in fixtures in initiate the driver from webDriverManager
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.hp = HomePage(self.driver) # creating an object of the home page class and passing the driver method
        self.hp.enterUserName()
        self.hp.enterPassword()
        self.hp.clickLogin()
        self.driver.close()

    def test_forgot_password(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.hp = HomePage(self.driver)  # creating an object of the home page class and passing the driver method
        self.hp.clickForgotPassword()
        self.hp.enterUserName()
        self.confmsg=self.hp.resetPassword()
        time.sleep(3)
        print(self.confmsg)
        if self.confmsg == 'Reset Password link sent successfully':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.getcwd()+"//forgot_password.png")
            self.driver.close()
            assert False

