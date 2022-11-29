from selenium.webdriver.common.by import By


class HomePage:
    text_username_name = 'username'
    text_password_name = 'password'
    btn_login_xpath ="//button[@type='submit']"
    linkText_forgotPass_xpath="//p[text()='Forgot your password? ']"
    def __init__(self, driver):
        self.driver = driver


    def enterUserName(self):
        self.driver.find_element(By.XPATH,self.text_username_name).clear()
        self.driver.find_element(By.XPATH, self.text_username_name).send_keys('Admin')

    def enterPassword(self):
        self.driver.find_element(By.LINK_TEXT,self.text_password_name).clear()
        self.driver.find_element(By.XPATH, self.text_password_name).send_keys('admin123')

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.btn_login_xpath).click()

    def clickForgotPassword(self):
        self.driver.find_element(By.XPATH,self.linkText_forgotPass_xpath).click()
