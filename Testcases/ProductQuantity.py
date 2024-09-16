import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.automationexercise.com/")

Verify_text = driver.find_element(By.XPATH, "//*[@id='slider-carousel']/div/div[1]/div[1]/h1/span").text
assert "Automation" in Verify_text
print("HomePage")


def PQuantity():
  product_element = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
  product_element.click()
  time.sleep(1)
  
  element = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/h2")
  element.location_once_scrolled_into_view
  time.sleep(2)
  
  view_product = driver.find_element(By.XPATH,
                                     "/html/body/section[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a")
  view_product.click()
  time.sleep(1)
  
  # increment = driver.find_element(By.XPATH, "//*[@id='quantity']")
  # increment.setUp(4)
  
  driver.execute_script("arguments[0].setAttribute('value','4')",
                        driver.find_element(By.XPATH, "//*[@id='quantity']"))
  time.sleep(2)
  
  AddtoCart = driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button/i")
  AddtoCart.click()
  time.sleep(1)
  
  ViewCart = driver.find_element(By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a")
  ViewCart.click()
  
  time.sleep(10)


PQuantity()