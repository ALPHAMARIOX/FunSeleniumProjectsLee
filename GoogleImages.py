from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Plans to use voice recognition for this later.
query = "Sailor Daisy"

service_obj = Service('C:\\Users\\AlphaMK\\Downloads\\chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get('https://images.google.com/')

time.sleep(5)
driver.find_element(By.XPATH, "//input[@name='q']").send_keys(query)
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.ENTER)


def scroll_to_bottom():
    last_height = driver.execute_script('\
    return document.body.scrollHeight')

    while True:
        driver.execute_script('\
        window.scrollTo(0,document.body.scrollHeight)')

        time.sleep(3)

        new_height = driver.execute_script('\
        return document.body.scrollHeight')

        try:
            driver.find_element(By.CSS_SELECTOR, ".YstHxe input").click()
            time.sleep(3)

        except:
            pass

        if new_height == last_height:
            break

        last_height = new_height


scroll_to_bottom()

for i in range(1, 50):
    try:
        img = driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[@class='T1diZc KWE8qe']/c-wiz[@class='FA7L0b P3Xfjc SSPGKf BIdYQ']/div[@class='mJxzWe']/div[@id='islmp']/div/div/div[contains(@class,'dMnSie tmS4cc blLOvc snjnxc')]/div[@class='gBPM8']/div[@class='eill-c']/span/div[@id='islrg']/div[@class='islrc']/div[" + str(i) + "]/a[" + str(i) + "]/div[" + str(i) + "]/img[" + str(i) + ")]")

        img.screenshot('Download-Location' + query + ' (' + str(i) + ').png')

        time.sleep(0.2)

    except:
        continue

driver.close()