import time
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()

options.add_experimental_option("excludeSwitches", ["enable-logging"])
print("testing started")
driver = webdriver.Chrome(options=options)

ExpectedTitle = "Most Reliable App & Cross Browser Testing Platform | Browserstack"

driver.get("https://www.browserstack.com/")
time.sleep(5)

ActualTitle = driver.title
print(ActualTitle)

if ActualTitle == ExpectedTitle:
    assert True

print("Success!")

# Find element using element's id attribute
# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# time.sleep(2)
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# time.sleep(2)
# driver.find_element(By.ID, "login-button").click()
# time.sleep(20)
#
# text = driver.find_element(By.CLASS_NAME, "title").text
#
# # Check if login was successful
# assert "products" in text.lower()
#
# print("TEST PASSED : LOGIN SUCCESSFUL")
#
# # Close the driver
driver.close()