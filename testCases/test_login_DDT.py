import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from ultilities.readProperites import ReadConfig
from ultilities.customLogger import LogGen
from ultilities import ExcelUtils


class Test_Login_002_DDT:

    baseURL = ReadConfig.getApplicationURL()
    path = ReadConfig.getTestDataPath()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    expected_login_title = ReadConfig.getExpected_login_title()
    expected_title = ReadConfig.getExpected_title()

    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("*********Test_Login_002_DDT***********")
        self.logger.info("*********test_login DDT:***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.row = ExcelUtils.getRowCount(self.path,'Sheet1')
        self.column = ExcelUtils.getColumnCount(self.path, 'Sheet1')

        list_Status = []

        for r in range(2,self.row+1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title = self.driver.title

            if act_title == self.expected_title:
                if self.exp == "Pass":
                    self.logger.info("***Passed1***")
                    self.lp.clickLogout()
                    list_Status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Failed1***")
                    self.lp.clickLogout()
                    list_Status.append("Fail")
            elif act_title != self.expected_title:
                if self.exp == "Pass":
                    self.logger.info("***Failed2***")
                    list_Status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***Failed3***")
                    list_Status.append("Pass")

        if "Fail" not in list_Status:
            self.logger.info("=> Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("=> Login DDT test failed")
            self.driver.close()
            assert False

        self.logger.info("End of Login DDT test done")
        self.logger.info("Completed Test_Login_002_DDT")





