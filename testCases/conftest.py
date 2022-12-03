import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import datetime

@pytest.fixture() # Decorator to mark a fixture factory function.This decorator can be used, with or without parameters, to define a fixture function.
def setup():
#    if browser=='edge':
        ser=Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=ser)
        return driver
    # else:
    # ser = Service(ChromeDriverManager().install())  # chromeDriverManager is a class and inside which there is a predefined method installed -install
    # driver = webdriver.Chrome(service=ser)
    # return driver
#
# def pytest_adoption(parser): # this would get the value from CLI/hooks
#     parser.adoption('--browser')
#
# @pytest.fixture()
# def browser(request): #This will return the browser value to setup method
#     return request.config.getoption('--browser')

## Pytest Html report ##

# It is hook for adding environment info to HTML Report

def pytest_configure(config):
        config._metadata['Project Name'] = 'Opencart'
        config._metadata['Module Name'] = 'CustRegistration'
        config._metadata['Tester'] = 'Pavan'



@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
        config.option.htmlpath = os.getcwd()+'/reports/'+datetime.now().strftime('%d-%m-%Y %H-%M-%S')+'.html'
