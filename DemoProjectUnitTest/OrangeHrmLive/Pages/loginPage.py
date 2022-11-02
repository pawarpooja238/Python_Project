from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.UserName_TextBox_Xpath = "//input[@name='username']"
        self.Password_TextBox_Xpath = "//input[@name='password']"
        self.LoginButton_xpath= "//button[@type='submit']"
        self.invalidLoginErr_xpath="//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def enterUsername(self,username):
        self.driver.find_element(By.XPATH, self.UserName_TextBox_Xpath).clear()
        self.driver.find_element(By.XPATH,self.UserName_TextBox_Xpath ).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.Password_TextBox_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Password_TextBox_Xpath).send_keys(password)

    def ClickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.LoginButton_xpath).click()

    def getTextInvalidLogin(self):
        msg = self.driver.find_element(By.XPATH, self.invalidLoginErr_xpath).text
        return msg









