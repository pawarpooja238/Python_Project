from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.WelcomeDropDown_Xpath = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
        self.LogOutBtn_xpath="//a[text()='Logout']"


    def clickOnWelcomeDropDown(self):
        self.driver.find_element(By.XPATH, self.WelcomeDropDown_Xpath).click()

    def clickOnLogout(self):
        self.driver.find_element(By.XPATH, self.LogOutBtn_xpath).click()
