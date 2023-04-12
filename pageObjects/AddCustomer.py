from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class AddCustomer :

    customer_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    sub_customer_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btn_AddNew_xpath = "(//a[normalize-space()='Add new'])[1]"
    email_id = "Email"
    password_id = "Password"
    firstName_id = "FirstName"
    lastName_id = "LastName"
    gender_Male_id = "Gender_Male"
    gender_Female_id = "Gender_Female"
    dateOfBirth_id = "DateOfBirth"
    company_id = "Company"
    newsletter_xpath= "(//div[@role='listbox'])[1]"
    # newsletter1_xpath = "//li[normalize-space()='Your store name']"
    newsletter1_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    newsletter2_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    managerVender_id = "VendorId"
    adminComment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"
    alert_success_xpath = "(//div[@class='alert alert-success alert-dismissable'])[1]"
    clearRole_xpath = '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]'
    missingRoleValidation_xpath = "//div[@class='content-wrapper']//li[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):

        self.driver.find_element(By.XPATH, self.customer_xpath).click()

        # self.driver.find_element(By.XPATH, self.sub_customer_xpath).click()
        # print("click sub customer successful")

        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")

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
            self.driver.find_element(By.ID, self.gender_Male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.gender_Female_id).click()
        else:
            self.driver.find_element(By.ID, self.gender_Female_id).click()

    def fillOutDateOfBirth (self, dateOfBirth):
        self.driver.find_element(By.ID, self.dateOfBirth_id).send_keys(dateOfBirth)

    def fillOutCompanyName (self, companyName):
        self.driver.find_element(By.ID, self.company_id).send_keys(companyName)

    def fillOutNewsletter (self, value):
        self.driver.find_element(By.XPATH, self.newsletter_xpath).click()
        time.sleep(0.5)
        if value == "Your store name":
            self.listitem = self.driver.find_element(By.XPATH, self.newsletter1_xpath)
        elif value == "Test store 2":
            self.listitem = self.driver.find_element(By.XPATH, self.newsletter2_xpath)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def selectCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(1)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.clearRole_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def selectMangerOfVender(self, value):
        drp = Select(self.driver.find_element(By.ID, self.managerVender_id))
        drp.select_by_visible_text(value)

    def writeAdminComment(self, value):
        self.driver.find_element(By.ID, self.adminComment_id).send_keys(value)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def clearRoleValue(self):
        self.driver.find_element(By.XPATH, self.clearRole_xpath ).click()





