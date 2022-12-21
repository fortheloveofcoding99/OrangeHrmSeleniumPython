import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures('setup')
class BaseClass:
    def getLogger(self):
         loggerName = inspect.stack()[1][3]
         logger = logging.getLogger(loggerName)
         fileHandlr=logging.FileHandler('logfile.log') # where all the logfile will be saved
         formatter = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s') #format to print
         fileHandlr.setFormatter(formatter) #casting the formatter to fileHandlr
         logger.addHandler(fileHandlr) # casting the filehandler to logger
         logger.setLevel(logging.INFO) # setting the level of logging
         return logger

    def elementVisible(self, loc):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, loc)))
        return element

    def selectOptionByText(self,loc,text):
        sel = Select(loc)
        sel.select_by_visible_text(text)

    def scrollDownByElement(self,loc):
        ele = driver.find_element(By.XPATH,loc)
        self.driver.execute_script('arguments[0].scrollIntoView();',ele)
