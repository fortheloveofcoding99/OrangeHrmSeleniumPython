import time

import pytest
from pageObjects.HomePage import HomePage # importing the UI elements of OrangeHrm homepage
import os
from utilities.readProperties import ReadConfig
from utilities.BaseClass import BaseClass


class Test_001_adminLogin(BaseClass):
    baseURL= ReadConfig.getApplicationUrl() # static method declaration in readProperties file


    @pytest.mark.sanity
    def test_login(self,setup): # setup method is present in fixtures in initiate the driver from webDriverManager
        log = self.getLogger()
        log.info("$$$login test case started$$$")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.hp = HomePage(self.driver) # creating an object of the home page class and passing the driver method
        self.hp.enterUserName()
        self.hp.enterPassword()
        self.hp.clickLogin()
        time.sleep(2)
        self.hp.checkHeader()
        self.driver.close()
        log.info("$$$login test case ended$$$")

    @pytest.mark.regression
    def test_forgot_password(self,setup):
        log = self.getLogger()
        log.info("$$$forgot Password test case started$$$")
        self.driver = setup
        self.driver.get(self.baseURL)

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
        log.info("$$$forgot password test case ended$$$")
