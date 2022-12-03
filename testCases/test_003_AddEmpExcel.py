import pytest
from pageObjects.Dashboard import Dashboard #importing the UI elements of OrangeHrm Dashboard
from pageObjects.HomePage import HomePage # importing the UI elements of OrangeHrm homepage
from pageObjects.PimPage import PimPage
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerate
from utilities import XlUtils

class Test_002_addEmployee:
    baseURL = ReadConfig.getApplicationUrl()  # static method declaration in readProperties file
    loggr = LogGenerate.loggen()  # for logging
    file = 'C:/Users/befor/PycharmProjects/OpenCartV1_Selenium_Python/testData/Book1.xlsx'

    def test_addEmpExcel(self,setup): # setup method is present in fixtures in initiate the driver from webDriverManager
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.image ='C:/Users/befor/Downloads/oraange.jpg'
        self.rows = XlUtils.getRowCount(self.file, 'EmpAdd')

        self.hp = HomePage(self.driver)     # creating an object of the home page class and passing the driver method
        self.db = Dashboard(self.driver)  # creating an object of the dashboard page class and passing the driver method
        self.pp = PimPage(self.driver)  # creating an object of the pim page class and passing the driver method
        self.hp.enterUserName()
        self.hp.enterPassword()
        self.hp.clickLogin()
        self.db = Dashboard(self.driver)  # creating an object of the dashboard page class and passing the driver method
        self.db.clickPIMTab()
        self.pp.hinzFugenAngstellter()
        for r in range(2,self.rows+1):
            self.Vname = XlUtils.readData(self.file, 'EmpAdd', r, 1)
            self.nname = XlUtils.readData(self.file, 'EmpAdd', r, 2)
            self.ausweis = XlUtils.readData(self.file, 'EmpAdd', r, 3)
            self.pp.hinzfugenVorname(self.Vname)
            self.pp.hinzfugenNachname(self.nname)
            self.pp.hinzfugenFoto(self.image)
            self.pp.hinzfugenAngstellterId(self.ausweis)
            self.pp.erstenSpeichern()
            self.pp.nachste_angstellter()




