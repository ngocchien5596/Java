from ast import If
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test():

    url = 'https://mavuno-web-staging.pula.cloud/homepage/'
    userName = 'chien'
    password = 'b8a3e00ec69da255115389c8'
    projectName = '24th Feb Chien'

    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Vào trang mavuno
    driver.get(url)
    time.sleep(1)

    # Nhập username
    driver.find_element(By.NAME,'username').send_keys(userName)

    # Nhập password
    driver.find_element(By.NAME,'password').send_keys(password)

    # Nhấn nút Login
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()

    # Nhấn vào General
    wait = WebDriverWait(driver,5)
    element = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='general']")))
    element.click()
    time.sleep(2)
    
    # Nhăn vào Unidashboard
    driver.find_element(By.XPATH,"//span[text()='Unidashboard']").click()
    time.sleep(2)

    # Tìm kiếm project
    driver.find_element(By.XPATH,"(//input[@placeholder='Search for project'])[1]").send_keys(projectName)
    time.sleep(5)

    # element = driver.find_element(By.ID,"CCE Preparation-tab")

    # If (element.get_attribute('innerHTML').text) != 'CCE Preparation(0)':

    # Nhấn vào tab CCE Ongoing
    driver.find_element(By.ID,"CCE Ongoing-tab").click()
    time.sleep(2)

    # Nhấn vào Project 24th Feb Chien
    driver.find_element(By.XPATH,"//span[contains(text(),'24th')]").click()
    time.sleep(3)

    # Nhấn chọn tab Project Actors
    driver.find_element(By.XPATH,"//span[text()='Project Actors']").click()
    time.sleep(2)

    

    driver.quit()
