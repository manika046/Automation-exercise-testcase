import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.automationexercise.com/")


# for login user with correct email and password
def Login():
  login_element = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
  login_element.click()
  time.sleep(5)
  
  # verify
  text = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/h2").text
  assert "Login to your account" in text
  print("TEST PASSED : SUCCESSFUL")
  
  email_element = driver.find_element(By.NAME, "email")
  email_element.send_keys("minie@gmail.com")
  time.sleep(1)
  
  password_element = driver.find_element(By.NAME, "password")
  password_element.send_keys("abcdefgh")
  time.sleep(1)
  
  login_button = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button")
  login_button.click()
  time.sleep(1)
  
  user_logged = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/p")
  assert user_logged.text == "Your email or password is incorrect!"
  print("Incorrect Email or Password")
  
  driver.close()


Login()