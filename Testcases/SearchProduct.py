import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.automationexercise.com/")

Verify_text = driver.find_element(By.XPATH, "//*[@id='slider-carousel']/div/div[1]/div[1]/h1/span").text
assert "Automation" in Verify_text
print("HomePage")


def Search():
  product_element = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
  product_element.click()
  time.sleep(1)
  
  Verify_pdp = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/h2").text
  assert "ALL PRODUCTS" in Verify_pdp
  print("Product Page")
  
  search_input = driver.find_element(By.ID, "search_product")
  search_input.send_keys("POLO")
  time.sleep(1)
  
  search_icon = driver.find_element(By.XPATH, "//*[@id='submit_search']/i")
  search_icon.click()
  time.sleep(1)
  
  Verify_search = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/h2")
  assert Verify_search.text == "SEARCHED PRODUCTS"
  print("Found Search Product")
  
  driver.close()


Search()