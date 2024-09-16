import time

from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")
# time.sleep(5)

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://test.fleetpanda.com/users/login")

driver.find_element(By.ID, "user_email").send_keys("9861550096")
driver.find_element(By.NAME, "user[password]").send_keys("Password")
driver.find_element(By.NAME, "commit").click()


time.sleep(20)