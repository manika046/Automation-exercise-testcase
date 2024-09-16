import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.automationexercise.com/")

Verify_text = driver.find_element(By.XPATH, "//*[@id='slider-carousel']/div/div[1]/div[1]/h1/span").text
assert "Automation" in Verify_text
print("HomePage")


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
  email_element.send_keys("miniepark@gmail.com")
  time.sleep(1)
  
  password_element = driver.find_element(By.NAME, "password")
  password_element.send_keys("abcdefgh")
  time.sleep(1)
  
  login_button = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button")
  login_button.click()
  
  user_logged = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a")
  assert user_logged.text == "Logged in as Minie"
  print("Login Successful!")
  
  delete = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")
  delete.click()
  time.sleep(2)
  
  driver.switch_to.window(driver.current_window_handle)
  
  delete_account = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/h2/b")
  assert delete_account.text == "ACCOUNT DELETED!"
  print("Account Deleted Successfully!")
  time.sleep(5)
  
  driver.close()


Login()