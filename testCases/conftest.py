import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import datetime
driver = None

@pytest.fixture() # Decorator to mark a fixture factory function.This decorator can be used, with or without parameters, to define a fixture function.
def setup():
    global driver
    # browser = request.config.getoption('browser')
    # if browser=='edge':
    ser = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=ser)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver
    # else:
    #  ser = Service(ChromeDriverManager().install())  # chromeDriverManager is a class and inside which there is a predefined method installed -install
    #  driver = webdriver.Chrome(service=ser)
    #  driver.maximize_window()
    #  driver.implicitly_wait(5)
    #  return driver
#
# def pytest_adoption(parser): # this would get the value from CLI/hooks
#     parser.addoption('--browser',action='store',default='chrome')
#
# @pytest.fixture()
# def browser(request): #This will return the browser value to setup method
#     return request.config.getoption('--browser')

## Pytest Html report ##

# It is hook for adding environment info to HTML Report

def pytest_configure(config):
        config._metadata['Project Name'] = 'Opencart'
        config._metadata['Module Name'] = 'CustRegistration'
        config._metadata['Tester'] = 'Som'



@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
        config.option.htmlpath = os.getcwd()+'/reports/'+datetime.now().strftime('%d-%m-%Y %H-%M-%S')+'.html'


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name ='reports/'+ report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = ('<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
