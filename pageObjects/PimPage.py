import time

from selenium.webdriver.common.by import By
from utilities.randomInt import random_number_generate
from utilities import XlUtils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PimPage:
    btn_add_xpath = "//button[text()=' Add ']"
    input_vorName_name = "firstName"
    input_zweiterVorName_name = "middleName"
    input_nachName_name = "lastName"
    input_angstellterId_xpath = "(//input[contains(@class,'oxd-input--active')])[5]"
    input_image_xpath = "//button[contains(@class,'employee-image-action')]"
    btn_erstenSave_xpath = "//button[@type='submit']"
    link_addEmp_xpath = "//a[text()='Add Employee']"
    link_addjob_xpath = "//a[text()='Job']"
    text_verifyEmp_xpath = "//h6[text()='Heidi Klum']"
    dropdown_jobTitle_xpath ="//div[@class='oxd-select-text-input']"
    dropdown_jobCategory_xpath = "(//div[@class='oxd-select-text-input'])[2]"
    dropdown_jobUnit_xpath = "(//div[@class='oxd-select-text-input'])[3]"
    dropdown_joblocation_xpath = "(//div[@class='oxd-select-text-input'])[4]"
    dropdown_jobEmpStat_xpath = "(//div[@class='oxd-select-text-input'])[5]"
    link_reportTo_xpath = "//a[text()='Report-to']"
    btn_managerAdd_xpath = "(//button[@type='button'])[2]"
    input_manager_xpath = "//input[@placeholder='Type for hints...']"
    dropdown_reportMethod_xpath = "//div[@class='oxd-select-text-input']"

    # image ='C:/Users/befor/Downloads/oraange.jpg'
    # file = 'C:/Users/befor/PycharmProjects/OpenCartV1_Selenium_Python/Book1.xlsx'
    # rows = XlUtils.getRowCount(file, 'EmpAdd')
    # for r in range(2,rows+1):
    #     Vname = XlUtils.readData(file,'EmpAdd',r,1)
    #     nname = XlUtils.readData(file,'EmpAdd',r,2)
    #     ausweis = XlUtils.readData(file,'EmpAdd',r,3)

    def __init__(self, driver):
        self.driver=driver

    def hinzFugenAngstellter(self):
        self.driver.find_element(By.XPATH,self.btn_add_xpath).click()

    def hinzfugenVorname(self, vname):
        self.driver.find_element(By.NAME,self.input_vorName_name).send_keys(vname)

    def hinzfugenNachname(self, nname):
        self.driver.find_element(By.NAME,self.input_nachName_name).send_keys(nname)

    def hinzfugenAngstellterId(self, ausweis):
        self.driver.find_element(By.XPATH, self.input_angstellterId_xpath).clear()
        self.driver.find_element(By.XPATH,self.input_angstellterId_xpath).send_keys(ausweis)

    def hinzfugenFoto(self,image):
        self.driver.find_element(By.XPATH,self.input_image_xpath).send_keys(image)

    def erstenSpeichern(self):
        self.driver.find_element(By.XPATH,self.btn_erstenSave_xpath).click()

    def sichrer_arbeit(self):
        pass

    def nachste_angstellter(self):
        self.driver.find_element(By.XPATH,self.link_addEmp_xpath).click()

    def berufzeichsnung(self):
        self.driver.find_element(By.XPATH,self.link_addjob_xpath).click()
        time.sleep(2)
        drop_down = []
        drop_down.append(self.driver.find_element(By.XPATH,self.dropdown_jobTitle_xpath))
        drop_down.append(self.driver.find_element(By.XPATH,self.dropdown_jobCategory_xpath))
        drop_down.append(self.driver.find_element(By.XPATH,self.dropdown_jobUnit_xpath))
        drop_down.append(self.driver.find_element(By.XPATH,self.dropdown_joblocation_xpath))
        drop_down.append(self.driver.find_element(By.XPATH, self.dropdown_jobEmpStat_xpath))
        for drop_down_element in drop_down:
            drop_down_element.click()
            drop_down_element.send_keys(Keys.DOWN)
            time.sleep(1)
            drop_down_element.send_keys(Keys.RETURN)
            time.sleep(1)
    def berichteAn(self, Bericht):
        self.driver.find_element(By.XPATH, self.link_reportTo_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_managerAdd_xpath).click()
        managerin = self.driver.find_element(By.XPATH, self.input_manager_xpath)
        managerin.send_keys(Bericht)
        time.sleep(1)
        managerin.send_keys(Keys.DOWN)
        time.sleep(1)
        managerin.submit()
        managerName = self.driver.find_element(By.XPATH, self.dropdown_reportMethod_xpath)
        managerName.click()
        managerName.send_keys(Keys.DOWN)
        time.sleep(1)
        managerName.send_keys(Keys.ENTER)




