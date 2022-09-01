from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service_obj = Service("C:\\Users\\AlphaMK\\Downloads\\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://twitter.com/i/flow/login")

driver.find_element(By.XPATH, '//input[@name="text"]').send_keys("Username")
driver.find_element(By.XPATH, '//input[@name="text"]').send_keys(Keys.ENTER)

time.sleep(2)

driver.find_element(By.XPATH, "//input[name='password']").send_keys("Password")
driver.find_element(By.XPATH, "//input[name='password']").send_keys(Keys.ENTER)


# Since my account has MFA (Multi-Factor Authentication, I will be notified on my phone about the confirmation code.
# Base code for this project is found on https://www.geeksforgeeks.org/login-twitter-using-python-selenium/
# Additional adjustments were made due to Twitter changing their website's front end and back end frequently, as most companies do.