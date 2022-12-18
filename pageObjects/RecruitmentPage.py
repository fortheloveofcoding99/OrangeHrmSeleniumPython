
import time

from selenium.webdriver.common.by import By
from utilities import XlUtils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class RecPage:
    input_Vorname_name = 'firstName'
    input_Nachname_name = 'lastName'
    input_email_xpath = "//input[@placeholder='Type here']"
    checkBox_zustimmung_xpath = "//i[contains(@class,'oxd-checkbox-input-icon')]"
    btn_add_xpath = "(//button[@type='button'])[3]"
    btn_erstenSave_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver=driver

    def hinzfugenKandidate(self,fname,lname,emaila):
        self.driver.find_element(By.XPATH,self.btn_add_xpath).click()
        self.driver.find_element(By.NAME,self.input_Vorname_name).send_keys(fname)
        self.driver.find_element(By.NAME,self.input_Nachname_name).send_keys(lname)
        self.driver.find_element(By.XPATH,self.input_email_xpath).send_keys(emaila)
        self.driver.find_element(By.XPATH,self.checkBox_zustimmung_xpath).click()
        self.driver.find_element(By.XPATH,self.btn_erstenSave_xpath).click()
        time.sleep(3)

