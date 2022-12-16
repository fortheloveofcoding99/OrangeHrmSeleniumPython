import pytest
from pageObjects.Dashboard import Dashboard #importing the UI elements of OrangeHrm Dashboard
from pageObjects.HomePage import HomePage # importing the UI elements of OrangeHrm homepage
from pageObjects.PimPage import PimPage
import os
from utilities.readProperties import ReadConfig
from utilities import XlUtils
from utilities.BaseClass import BaseClass


class Test_002_addEmployee(BaseClass):
    baseURL = ReadConfig.getApplicationUrl()  # static method declaration in readProperties file

    @pytest.mark.sanity
    def test_addEmployee(self,setup): # setup method is present in fixtures in initiate the driver from webDriverManager
        log = self.getLogger()
        self.driver = setup
        self.driver.get(self.baseURL)

        self.hp = HomePage(self.driver)  # creating an object of the home page class and passing the driver method
        self.hp.enterUserName()
        self.hp.enterPassword()
        self.hp.clickLogin()
        self.db = Dashboard(self.driver)  # creating an object of the dashboard page class and passing the driver method
        self.db.clickPIMTab()
        self.pp = PimPage(self.driver)  # creating an object of the home page class and passing the driver method
        self.pp.hinzFugenAngstellter()
        self.pp.hinzfugenVorname('Heidi')
        self.pp.hinzfugenNachname('Klum')
        self.pp.hinzfugenFoto('C:/Users/befor/PycharmProjects/OpenCartV1_Selenium_Python/oraange.jpg')
        self.pp.hinzfugenAngstellterId(2129)
        self.pp.erstenSpeichern()
        self.elementVisible(self.pp.text_verifyEmp_xpath)
        self.pp.berufzeichsnung()
        self.pp.erstenSpeichern()
