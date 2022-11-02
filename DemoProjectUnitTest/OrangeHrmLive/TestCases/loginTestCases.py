from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest

from OrangeHrmLive.Pages.homePage import HomePage
from OrangeHrmLive.Pages.loginPage import LoginPage


class LoginTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        Service_obj = Service("C:/Users/dayanand.mhetre/PycharmProjects/PythonSeleniumFrameWork/Driver/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=Service_obj)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # def test_loginWithValidCre(self):
    #     driver = self.driver
    #     driver.get("https://opensource-demo.orangehrmlive.com")
    #
    #     loginP = LoginPage(driver)
    #     loginP.enterUsername("Admin")
    #     loginP.enterPassword("admin123")
    #     loginP.ClickOnSubmit()
    #
    #     home = HomePage(driver)
    #     home.clickOnWelcomeDropDown()
    #     home.clickOnLogout()
    #
    #     print("Test successfully competed")

    def test_loginWithInValidCre(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        loginP = LoginPage(driver)
        loginP.enterUsername("Admin123")
        loginP.enterPassword("admin123123")
        loginP.ClickOnSubmit()
        message = driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
        self.assertEqual(message,"Invalid credentials")
        print("Test successfully competed")
        self.assertTrue()

        # self.driver.implicitly_wait(10)
        # self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        # self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # self.driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        # self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test complete")
