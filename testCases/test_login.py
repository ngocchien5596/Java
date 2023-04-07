import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from ultilities.readProperites import ReadConfig
from ultilities.customLogger import LogGen


class Test_Login_001:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    expected_login_title = ReadConfig.getExpected_login_title()
    expected_title = ReadConfig.getExpected_title()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*********Test_Login_001:***********")
        self.logger.info("*********test_homePageTitle:***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # print("\n"+ act_title)
        if act_title == self.expected_login_title:
            self.logger.info("*********Home page title is passed ***********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/"+"test_homePageTitle.png")
            self.logger.error("*********Home page title is failed ***********")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("*********test_login:***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_bannerText = self.driver.find_element(By.XPATH, LoginPage.homePage_bannerText_xpath).text
        if act_bannerText == self.expected_title:
            self.logger.info("*********test login is passed ***********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.logger.error("*********test login is failed ***********")
            self.driver.close()
            assert False


