from pageObjects.SearchCustomerPage import SearchCustomer
from ultilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from ultilities.readProperites import ReadConfig
from selenium.webdriver.common.by import By
import pytest
import time

class TestSearchCustomer:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    act_email_xpath = '//*[@id="customers-grid"]/tbody/tr[1]/td[2]'
    def test_SearchCustomer_By_Email(self, setup):

        self.logger.info("*************************************")

        self.logger.info("*** Start Test search customer by valid email ***")

        # Khoi tao driver
        self.driver = setup

        # Vao link
        self.driver.get(self.baseURL)

        # Cai max screen
        self.driver.maximize_window()

        # Goi class LoginPage
        self.lp = LoginPage(self.driver)
        # Nhap user
        self.lp.setUserName(self.username)
        # Nhap password
        self.lp.setPassword(self.password)
        # Click login
        self.lp.clickLogin()

        # Di vao menu Customers/Customers
        self.ac = AddCustomer(self.driver)
        self.ac.clickOnCustomerMenu()

        self.logger.info("*** Login successful ***")

        # Goi class SearchCustomer
        self.sc = SearchCustomer(self.driver)

        exp_email = "kiyjcycyhjc"

        # Goi ham fillOutEmailSearch de dien email
        self.sc.fillOutEmailSearch(exp_email)
        # Click Search
        self.sc.clickSearchButton()
        self.logger.info("*** Searching ***")
        time.sleep(2)
        noValueMessage = self.driver.find_element(By.XPATH,self.sc.noValue_xpath).text
        if "No data available in table" in noValueMessage:
            self.logger.error("*** No data is displayed => FAILED ***")
            self.driver.close()
            assert False
        else:
            list_Status = []
            list_Email = []
            for r in range(1, self.sc.getNumOfRow() + 1):
                table = self.driver.find_element(By.ID, self.sc.table_id)

                emailid = (table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[2]").text).split('@')[0]
                list_Email.append(emailid)


                if exp_email in emailid:
                    list_Status.append("Pass")
                else:
                    list_Status.append("Fail")

            if "Fail" not in list_Status:
                self.logger.info("*** Be able to search with valid email => PASSED ***")
                self.driver.close()
                assert True
            else:
                self.logger.error("*** Result is incorrect => FAILED ***")
                self.driver.close()
                assert False

            print(list_Email)
        self.logger.info("*** Test search customer by email Finished ***")


