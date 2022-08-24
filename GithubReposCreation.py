from selenium import webdriver
from selenium.webdriver.common.by import By


# I have MFA on my Github account, so, it would be more difficult to automate it with Selenium, but it will be easier for those without MFA.
driver = webdriver.Chrome('C:\\Users\\AlphaMK\\Downloads\\chromedriver')


def github_repo(username, password, repository_name, descriptions=False, private=False, readme=False):
    driver.get('https://github.com/login')

    driver.find_element(By.XPATH, '//*[@id="login_field"').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"').send_keys(password)

    driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/input[14]').click()

    driver.find_element(By.XPATH, '//*[@id="repos-container"]/h2/a').click()

    driver.find_element(By.XPATH, '//*[@id="repository_name"]').send_keys(repository_name)

    if descriptions:
        driver.find_element(By.XPATH, '//*[@id="repository_description"]').send_keys(descriptions)

    if private:
        driver.find_element(By.XPATH, '//*[@id="repository_visibility_private"]').click()

    if readme:
        driver.find_element(By.XPATH, '//*[@id="repository_auto_init"]').click()


github_repo("Username", "Password", "Repository Name")