import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://automationexercise.com")


def TestCase():
  driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div/div[1]/div/div[1]/div[1]/a[1]/button").click()
  time.sleep(2)
  
  text = driver.find_element(By.XPATH, "/html/body/section/div/div[1]/div/h2/b/a/span")
  assert text.text == "TEST"
  print("Success!")


TestCase()