import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://automationexercise.com")


def Contact_Us():
  contact_us = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[8]/a")
  contact_us.click()
  time.sleep(1)
  
  verify_text = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/h2")
  assert verify_text.text == "GET IN TOUCH"
  print("Clicked!")
  time.sleep(1)
  
  name_element = driver.find_element(By.NAME, "name")
  name_element.send_keys("Minie")
  time.sleep(1)
  
  email_element = driver.find_element(By.NAME, "email")
  email_element.send_keys("miniepark@gmail.com")
  time.sleep(1)
  
  subject_element = driver.find_element(By.NAME, "subject")
  subject_element.send_keys("Me")
  time.sleep(1)
  
  message_element = driver.find_element(By.ID, "message")
  message_element.send_keys("Hello")
  time.sleep(1)
  
  submit_button = driver.find_element(By.NAME, "submit")
  submit_button.click()
  time.sleep(2)
  
  driver.switch_to.alert.accept()
  time.sleep(1)
  
  success_text = driver.find_element(By.XPATH, "//*[@id='contact-page']/div[2]/div[1]/div/div[2]")
  assert success_text.text == "Success! Your details have been submitted successfully."
  print("Message Sent")
  
  Home_button = driver.find_element(By.XPATH, "//*[@id='form-section']/a/span")
  Home_button.click()
  time.sleep(1)
  
  print("Success!")
  
  driver.close()


Contact_Us()
