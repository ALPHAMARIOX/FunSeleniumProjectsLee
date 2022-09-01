from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service_obj = Service("C:\\Users\\AlphaMK\\Downloads\\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://twitter.com/i/flow/login")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input[name='text']").send_keys("Username")
driver.find_element(By.CSS_SELECTOR, "input[name='text']").send_keys(Keys.ENTER)

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Password")
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(Keys.ENTER)