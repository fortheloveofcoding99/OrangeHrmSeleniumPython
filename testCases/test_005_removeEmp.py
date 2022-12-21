import time

import pytest
from pageObjects.Dashboard import Dashboard #importing the UI elements of OrangeHrm Dashboard
from pageObjects.HomePage import HomePage # importing the UI elements of OrangeHrm homepage
from pageObjects.PimPage import PimPage
import os
from utilities.readProperties import ReadConfig
from utilities.BaseClass import BaseClass

class Test_005_RemoveEmployee(BaseClass):
    baseURL = ReadConfig.getApplicationUrl()  # static method declaration in readProperties file


    @pytest.mark.sanity
    def test_removeEmployee(self,setup):  # setup method is present in fixtures in initiate the driver from webDriverManager and getdata is like a data provider at the bottom of this module
        log = self.getLogger()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)  # creating an object of the home page class and passing the driver method
        self.db = Dashboard(self.driver)  # creating an object of the dashboard page class and passing the driver method
        self.pp = PimPage(self.driver)  # creating an object of the pim page class and passing the driver method
        self.hp.enterUserName()
        self.hp.enterPassword()
        self.hp.clickLogin()
        self.db = Dashboard(self.driver)  # creating an object of the dashboard page class and passing the driver method
        self.db.clickPIMTab()
 #       self.scrollDownByElement(self.pp.table_allEmps_xpath)
 #       time.sleep(5)
        self.pp.entfernenAngstellter()


