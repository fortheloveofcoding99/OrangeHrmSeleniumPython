import pytest
from pageObjects.Dashboard import Dashboard #importing the UI elements of OrangeHrm Dashboard
from pageObjects.HomePage import HomePage # importing the UI elements of OrangeHrm homepage
from pageObjects.RecruitmentPage import RecPage
import os
from utilities.readProperties import ReadConfig
from utilities.BaseClass import BaseClass

class Test_004_AddIntCandidate(BaseClass):
    baseURL = ReadConfig.getApplicationUrl()  # static method declaration in readProperties file

    @pytest.mark.sanity
    def test_addInterviewCandidate(self,getData,setup): # setup method is present in fixtures in initiate the driver from webDriverManager and getdata is like a data provider at the bottom of this module
        log = self.getLogger()
        self.driver = setup
        self.driver.get(self.baseURL)

        self.hp = HomePage(self.driver)  # creating an object of the home page class and passing the driver method
        self.hp.enterUserName()
        self.hp.enterPassword()
        self.hp.clickLogin()
        self.db = Dashboard(self.driver)  # creating an object of the dashboard page class and passing the driver method
        self.db.clickRecruitmentTab()
        self.rp = RecPage(self.driver) # creating an object of the recruitment page class and passing the driver method
        self.rp.hinzfugenKandidate(getData['vornam'],getData['nacnam'],getData['emaild']) # paasing the data from the getData method
        self.driver.close()

    @pytest.fixture(params=[{'vornam':'Karim','nacnam':'Benzema','emaild':'benzema@fifa.com'},{'vornam':'Didier','nacnam':'Drogba','emaild':'drogba@fifa.com'}]) # adding elements in the dictionary to be passed into the test case
    def getData(self,request):
        return request.param
