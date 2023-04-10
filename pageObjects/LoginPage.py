from selenium.webdriver.common.by import By
from ultilities.readProperites import ReadConfig
class LoginPage:
    textbox_username_id = "Username"
    textbox_password_id = "Password"
    button_login_xpath = "(//input[@value='Log in'])[1]"
    button_user_xpath = "(//*[name()='svg'])[3]"
    button_logout_xpath = "(//span[normalize-space()='Log out'])[1]"
    homePage_bannerText_xpath = "(//h1[normalize-space()='Free and open-source eCommerce platform'])[1]"

    baseURL = ReadConfig.getApplicationURL()
    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        # print("a")
        # self.driver.find_element(By.XPATH, self.button_user_xpath).click()
        # print("b")
        # self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
        # print("c")
        self.driver.get(self.baseURL)
