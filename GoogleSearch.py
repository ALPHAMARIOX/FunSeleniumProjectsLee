from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service('C:\\Users\\AlphaMK\\Downloads\\chromedriver')
driver = webdriver.Chrome(service=service_obj)

keyword = "Mann Vs. Machine"

driver.get("https://google.ca/search?q=" + keyword)