import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.automationexercise.com/")

Verify_text = driver.find_element(By.XPATH, "//*[@id='slider-carousel']/div/div[1]/div[1]/h1/span").text
assert "Automation" in Verify_text
print("HomePage")


def subscription():
  # subscription_element = driver.find_element(By.XPATH, "//*[@id='footer']/div[1]/div/div/div[2]/div/h2")
  # subscription_element.location_once_scrolled_into_view
  driver.execute_script("window.scrollTo(0, document.body);")
  
  element = driver.find_element(By.XPATH, "//*[@id='footer']/div[1]/div/div/div[2]/div/h2")
  assert element.text == "SUBSCRIPTION"
  print("Reach Subscription Section!")
  
  input_element = driver.find_element(By.ID, "susbscribe_email")
  input_element.send_keys("minie@gmail.com")
  time.sleep(1)
  
  input_icon = driver.find_element(By.XPATH, "//*[@id='subscribe']/i")
  input_icon.click()
  time.sleep(1)
  
  verify_subscribe = driver.find_element(By.XPATH, "//*[@id='success-subscribe']/div")
  assert verify_subscribe.text == "You have been successfully subscribed!"
  print("Successfully Subscribe")
  time.sleep(2)


subscription()