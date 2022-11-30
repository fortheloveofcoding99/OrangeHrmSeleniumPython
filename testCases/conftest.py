import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture() # Decorator to mark a fixture factory function.This decorator can be used, with or without parameters, to define a fixture function.
def setup():
    ser=Service(ChromeDriverManager().install()) # chromeDriverManager is a class and inside which there is a predefined method installed -install
    driver = webdriver.Chrome(service=ser)
    return driver