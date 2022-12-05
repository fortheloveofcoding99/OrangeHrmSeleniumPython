from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located(locator=loc))

wait.until(EC.element_to_be_clickable(locator=loc))

wait.until(EC.element_to_be_selected(locator=loc))
