import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.automationexercise.com/")

Verify_text = driver.find_element(By.XPATH, "//*[@id='slider-carousel']/div/div[1]/div[1]/h1/span").text
assert "Automation" in Verify_text
print("HomePage")


def RegisterWhileCheckout():
  product_element = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
  product_element.click()
  time.sleep(1)
  
  element = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/h2")
  element.location_once_scrolled_into_view
  
  clickable = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]")
  ActionChains(driver) \
    .click(clickable) \
    .perform()
  time.sleep(2)
  
  add_cart = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/a")
  add_cart.click()
  time.sleep(2)
  
  driver.find_element(By.XPATH, "//*[@id='cartModal']/div/div/div[3]/button").click()
  
  clicked = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[3]/div/div[1]/div[2]")
  ActionChains(driver) \
    .click(clicked) \
    .perform()
  time.sleep(2)
  
  new_cart = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/a")
  new_cart.click()
  time.sleep(2)
  
  driver.find_element(By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a/u").click()
  time.sleep(5)
  
  Proceed_Button = driver.find_element(By.XPATH, "//*[@id='do_action']/div[1]/div/div/a")
  Proceed_Button.click()
  
  Register_Element = driver.find_element(By.XPATH, "//*[@id='checkoutModal']/div/div/div[2]/p[2]/a/u")
  Register_Element.click()


RegisterWhileCheckout()