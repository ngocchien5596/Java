from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class AddCustomer :

    customer_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    sub_customer_xpath = "(//p[contains(text(),'Customers')])[2]"
    btn_AddNew_xpath = "(//a[normalize-space()='Add new'])[1]"
    email_id = "mail"
    password_id = "Password"
    firstName_id = "FirstName"
    lastName_id = "LastName"
    gender_Male_xpath = "//input[@id='Gender_Male']"
    gender_Female_xpath = "//input[@id='Gender_Female']"
    dateOfBirth_id = "DateOfBirth"
    company_id = "Company"
    newsletter_id = "SelectedNewsletterSubscriptionStoreIds"



    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.customer_xpath).click()
        self.driver.find_element(By.XPATH, self.sub_customer_xpath).click()

    def clickAddNew(self):
        self.driver.find_element(By.XPATH, self.btn_AddNew_xpath).click()

    def fillOutEmail(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def fillOutPassword(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def fillOutFirstName(self, firstName):
        self.driver.find_element(By.ID, self.firstName_id).send_keys(firstName)

    def fillOutLastName(self, lastName):
        self.driver.find_element(By.ID, self.lastName_id).send_keys(lastName)

    def selectGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.gender_Male_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.gender_Female_xpath).click()
        else:
            self.driver.find_element(By.ID, self.gender_Female_xpath).click()

    def fillOutDateOfBirth (self, dateOfBirth):
        self.driver.find_element(By.ID, self.dateOfBirth_id).send_keys(dateOfBirth)

    def fillOutCompanyName (self, companyName):
        self.driver.find_element(By.ID, self.dateOfBirth_id).send_keys(companyName)

    def fillOutNewsletter (self, value):
        drp = Select(self.driver.find_element(By.ID, self.newsletter_id))
        drp.select_by_visible_text(value)

    def selectCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)







