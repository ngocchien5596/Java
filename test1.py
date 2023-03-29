from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://mavuno-web-staging.pula.cloud")
    # time.sleep(3)

    # Input to User
    user = driver.find_element(By.NAME,"username")
    user.send_keys("chien")
    time.sleep(1)

    # Input to Password
    user = driver.find_element(By.NAME,"password")
    user.send_keys("b8a3e00ec69da255115389c8")
    time.sleep(1)

    # Press Login
    login_button = driver.find_element(By.CLASS_NAME,"button.is-primary")
    login_button.click()
    time.sleep(8)

    logo = driver.find_element(By.CLASS_NAME,"admin-logo")
    logo1= (By.CLASS_NAME,"admin-logo")

    # # Wait for Logo visibled
    # driver.implicitly_wait(EC.visibility_of_element_located(logo1))

    # Check login successfully
    assert driver.find_element(By.CLASS_NAME,"admin-logo").is_displayed()

    # Enter Unidashboard
    driver.find_element(By.CLASS_NAME,"aside.is-placed-left.is-expanded > menu-container.ps > menu.is-menu-main > menu-label").click()
    driver.find_element(By.CLASS_NAME,"menu-item-label").click()

    # Search project
    driver.find_element(By.CLASS_NAME,"control.is-clearfix > input").click()
    driver.find_element(By.CLASS_NAME,"control.is-clearfix > input").send_keys("chientest1")
    time.sleep(5)
    
    
    # # Logout
    # driver.find_element(By.CLASS_NAME,"is-user-name").click()
    # time.sleep(1)
    # driver.find_element(By.CLASS_NAME,"mdi.mdi-logout.default").click()
    # time.sleep(3)

    # # Check logout successfully
    # assert driver.find_element(By.CLASS_NAME,"button.is-primary").is_displayed()

    driver.quit()
