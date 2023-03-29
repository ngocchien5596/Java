from selenium.webdriver.support.ui import Select
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import random
from selenium.webdriver.common.by import By
import time

def test():
  
  random_char = str(random.randrange(1000,99999))

  email = "buingocchien" + random_char
  password = "traikimnguu5596"
  phone = "0866049211"
  url = "https://accounts.google.com/SignUp"
  print(email)
  
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.get (url)
  
  # Fill Họ
  driver.find_element(By.ID,"lastName").send_keys("Bùi")

  # Fill Tên
  driver.find_element(By.ID,"firstName").send_keys("Ngọc Chiến")

  # Fill Tên người dùng
  driver.find_element(By.ID,"username").send_keys(email)

  # Fill Mật khẩu
  driver.find_element(By.NAME,"Passwd").send_keys(password)

  # Fill Xác nhận mật khẩu
  driver.find_element(By.NAME,"ConfirmPasswd").send_keys(password)

  time.sleep(1)

  # Click Tiếp theo
  driver.find_element(By.XPATH,"//span[text()='Tiếp theo']").click()

  time.sleep(5)

  # Fill Số điện thoại
  driver.find_element(By.ID,"phoneNumberId").send_keys(phone)

   # Click Tiếp theo
  driver.execute_script('document.querySelector(".VfPpkd-vQzf8d").click()')

  time.sleep(20)

  # Fill ngày
  driver.find_element(By.ID,"day").send_keys("5")
  time.sleep(2)

  # Fill ngày
  driver.find_element(By.XPATH,"//select[@id='month']//child::option[2]").click()
  time.sleep(2)
   # Fill ngày
  driver.find_element(By.ID,"year").send_keys("1996")
  time.sleep(2)
  
    # Fill Giới tính
  driver.find_element(By.XPATH,'//*[@id="gender"]/option[2]').click()
  time.sleep(2)
  

   # Click Tiếp theo
  driver.find_element(By.XPATH,"//span[text()='Tiếp theo']").click()
  time.sleep(2)

  # Click Tôi đồng ý
  driver.find_element(By.XPATH,"//span[text()='Tôi đồng ý']").click()
  time.sleep(5)

  #  # Click Tiếp theo
  # driver.find_element(By.XPATH,"//span[text()='Tiếp theo']").send_keys("Keys.PAGE_DOWN")

   # Click Tiếp theo
  driver.find_element(By.XPATH,"//span[text()='Tiếp theo']").click()
  time.sleep(5)

  driver.quit()