import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.automationexercise.com/")

Verify_text = driver.find_element(By.XPATH, "//*[@id='slider-carousel']/div/div[1]/div[1]/h1/span").text
assert "Automation" in Verify_text
print("HomePage")


def Pdp_Verify():
  product_element = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
  product_element.click()
  time.sleep(1)
  
  Verify_pdp = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/h2").text
  assert "ALL PRODUCTS" in Verify_pdp
  print("Product Page")
  
  view_product = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/ul/li/a")
  view_product.click()
  
  driver.close()


Pdp_Verify()