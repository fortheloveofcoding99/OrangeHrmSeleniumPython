from selenium.webdriver.common.by import By
from utilities.randomInt import random_number_generate
from utilities import XlUtils


class PimPage:
    btn_add_xpath = "//button[text()=' Add ']"
    input_vorName_name = "firstName"
    input_zweiterVorName_name = "middleName"
    input_nachName_name = "lastName"
    input_angstellterId_xpath = "(//input[contains(@class,'oxd-input--active')])[5]"
    input_image_xpath = "//button[contains(@class,'employee-image-action')]"
    btn_erstenSave_xpath = "//button[@type='submit']"
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

