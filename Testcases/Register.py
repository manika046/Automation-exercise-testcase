import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.automationexercise.com/")


def RegisterUser():
  register_element = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
  register_element.click()
  time.sleep(5)
  
  # verify
  text = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/h2").text
  assert "New User Signup!" in text
  print("TEST PASSED : SUCCESSFUL")
  
  name_element = driver.find_element(By.NAME, "name")
  name_element.send_keys("Minie")
  time.sleep(1)
  
  email_element = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]")
  email_element.send_keys("miniepark@gmail.com")
  time.sleep(1)
  
  signup_button = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/button")
  signup_button.click()
  
  driver.switch_to.window(driver.current_window_handle)
  
  AText = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div[1]/h2/b")
  assert AText.text == "ENTER ACCOUNT INFORMATION"
  print("CLICKED")
  time.sleep(2)
  
  password_element = driver.find_element(By.ID, "password")
  password_element.send_keys("abcdefgh")
  
  dropdown = Select(driver.find_element(By.ID, "days"))
  dropdown.select_by_value("20")
  time.sleep(1)
  
  dropdown = Select(driver.find_element(By.ID, "months"))
  dropdown.select_by_value("10")
  time.sleep(1)
  
  dropdown = Select(driver.find_element(By.ID, "years"))
  dropdown.select_by_value("1999")
  time.sleep(1)
  
  Newsletter = driver.find_element(By.XPATH, "//*[@id='newsletter']")
  Newsletter.click()
  time.sleep(1)
  
  offer = driver.find_element(By.XPATH, "//*[@id='optin']")
  offer.click()
  time.sleep(1)
  
  FirstName = driver.find_element(By.ID, "first_name")
  FirstName.send_keys("Minie")
  time.sleep(1)
  
  LastName = driver.find_element(By.ID, "last_name")
  LastName.send_keys("Park")
  time.sleep(1)
  
  company_element = driver.find_element(By.ID, "company")
  company_element.send_keys("Flee")
  time.sleep(1)
  
  address_element = driver.find_element(By.NAME, "address1")
  address_element.send_keys("byasi")
  time.sleep(1)
  
  country = Select(driver.find_element(By.ID, "country"))
  country.select_by_value("United States")
  time.sleep(1)
  
  state = driver.find_element(By.ID, "state")
  state.send_keys("Bagmati")
  time.sleep(1)
  
  city = driver.find_element(By.ID, "city")
  city.send_keys("bkt")
  time.sleep(1)
  
  zipcode = driver.find_element(By.ID, "zipcode")
  zipcode.send_keys("022")
  
  number = driver.find_element(By.ID, "mobile_number")
  number.send_keys("123456")
  time.sleep(1)
  
  create_button = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div[1]/form/button")
  create_button.click()
  time.sleep(20)
  
  driver.switch_to.window(driver.current_window_handle)
  
  text_verify = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/h2/b")
  assert text_verify.text == "ACCOUNT CREATED!"
  print("Account Created")
  
  continue_button = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/a")
  continue_button.click()
  time.sleep(2)
  
  driver.switch_to.window(driver.current_window_handle)
  
  user_logged = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a")
  assert user_logged.text == "Logged in as Minie"
  print("Login Successful!")
  
  # delete = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")
  # delete.click()
  # time.sleep(2)
  #
  # driver.switch_to.window(driver.current_window_handle)
  #
  # delete_account = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/h2/b")
  # assert delete_account.text == "ACCOUNT DELETED!"
  # print("Account Deleted Successfully!")
  # time.sleep(5)
  
  driver.close()


RegisterUser()