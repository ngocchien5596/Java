from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from pageObjects.AddCustomer import AddCustomer

class SearchCustomer:

    email_id = "SearchEmail"
    firstName_id = "SearchFirstName"
    lastName_id = "SearchLastName"
    searchButton_id = "search-customers"
    table_id = "customers-grid"
    row_xpath = "//table[@id='customers-grid']//tbody/tr"
    column_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    noValue_xpath = "//*[@id='customers-grid']//tbody/tr/td"



    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        # self.ac = AddCustomer(self.driver)

        self.driver.find_element(By.XPATH, AddCustomer.customer_xpath).click()

        # self.driver.find_element(By.XPATH, self.sub_customer_xpath).click()
        # print("click sub customer successful")

        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
    def fillOutEmailSearch (self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def fillOutFirstNameSearch (self, firstName):
        self.driver.find_element(By.ID, self.email_id).send_keys(firstName)

    def fillOutLastNameSearch(self, lastName):
        self.driver.find_element(By.ID, self.email_id).send_keys(lastName)

    def clickSearchButton(self):
        self.driver.find_element(By.ID, self.searchButton_id).click()

    def getNumOfRow(self):
        return len(self.driver.find_elements(By.XPATH, self.row_xpath))

    def getNumOfCol(self):
        return len(self.driver.find_elements(By.XPATH, self.column_xpath))

    # def searchCustomerByEmail(self, email):
    #     flag = False
    #     for r in range(1, self.getNumOfRow()+1):
    #         table = self.driver.find_element(By.XPATH, self.table_id)
    #         emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
    #         if email == emailid:
    #             flag = True
    #             break
    #     return flag