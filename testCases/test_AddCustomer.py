import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import  AddCustomer
from selenium.webdriver.common.by import By
from ultilities.readProperites import ReadConfig
from ultilities.customLogger import LogGen
import string
import random
class Test_Add_Customer:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_01(self, setup):
        self.logger.info("***** Test add new customer full flow SUCCESS *****")

        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login successful ***")

        self.ac = AddCustomer(self.driver)
        self.ac.clickOnCustomerMenu()
        self.ac.clickAddNew()
        self.logger.info("*** Start to provide customer information ***")

        self.email = self.get_random_string(8) + "@gmail.com"
        self.logger.info("*** Email is " + self.email + " ***")

        self.ac.fillOutEmail(self.email)
        time.sleep(1)
        self.ac.fillOutPassword("test123")
        time.sleep(1)
        self.ac.fillOutFirstName("Ngoc")
        time.sleep(1)
        self.ac.fillOutLastName("Chien")
        time.sleep(1)
        self.ac.selectGender("Male")
        time.sleep(1)
        self.ac.fillOutDateOfBirth("05/05/1996")
        time.sleep(1)
        self.ac.fillOutCompanyName("Flying Emirates")
        time.sleep(1)
        self.ac.fillOutNewsletter("Your store name")
        time.sleep(1)
        self.ac.selectCustomerRoles("Vendors")
        time.sleep(1)
        self.ac.selectMangerOfVender("Vendor 1")
        time.sleep(1)
        self.ac.writeAdminComment("here is comment")
        time.sleep(1)
        self.ac.clickSave()
        time.sleep(0.5)

        self.logger.info("*** Click Save ***")
        self.alert = self.driver.find_element(By.XPATH, AddCustomer.alert_success_xpath).text

        if "The new customer has been added successfully" in self.alert:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_01.png")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")
        self.logger.info("*** Save successful ***")

    def test_02(self, setup):
        self.logger.info("***** Test add new customer without Customer Roles *****")

        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login successful ***")

        self.ac = AddCustomer(self.driver)
        self.ac.clickOnCustomerMenu()
        self.ac.clickAddNew()
        self.logger.info("*** Start to provide customer information ***")

        self.email = self.get_random_string(8) + "@gmail.com"
        self.logger.info("*** Email is " + self.email + " ***")

        self.ac.fillOutEmail(self.email)
        time.sleep(1)
        self.ac.fillOutPassword("test123")
        time.sleep(1)
        self.ac.fillOutFirstName("Ngoc")
        time.sleep(1)
        self.ac.fillOutLastName("Chien")
        time.sleep(1)
        self.ac.selectGender("Male")
        time.sleep(1)
        self.ac.fillOutDateOfBirth("05/05/1996")
        time.sleep(1)
        self.ac.fillOutCompanyName("Flying Emirates")
        time.sleep(1)
        self.ac.fillOutNewsletter("Your store name")
        time.sleep(1)
        self.ac.clearRoleValue()
        time.sleep(1)
        self.ac.selectMangerOfVender("Vendor 1")
        time.sleep(1)
        self.ac.writeAdminComment("here is comment")
        time.sleep(1)
        self.ac.clickSave()
        time.sleep(0.5)

        self.logger.info("*** Click Save ***")
        self.alert = self.driver.find_element(By.XPATH, AddCustomer.missingRoleValidation_xpath).text

        if "Add the customer to 'Guests' or 'Registered' customer role" in self.alert:
            assert True
            self.logger.info("********* Validation test Passed *********")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_02.png")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")
        self.logger.info("*** Save successful ***")

    def get_random_string(self, length):
        result = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
        return result