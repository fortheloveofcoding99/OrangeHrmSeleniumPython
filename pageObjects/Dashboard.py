from selenium.webdriver.common.by import By

class Dashboard:
    navBar_Admin_xpath = "//span[text()='Admin']"
    navBar_Dashbod_xpath = "//span[text()='Dashboard']"
    navBar_PIM_xpath= "//span[text()='PIM']"

    def clickAdminTab(self):
        self.driver.find_element(By.XPATH,self.navBar_Admin_xpath).click()

    def clickDashboardTab(self):
        self.driver.find_element(By.XPATH, self.navBar_Dashbod_xpath).click()

    def clickPIMTab(self):
        self.driver.find_element(By.XPATH, self.navBar_PIM_xpath).click()
