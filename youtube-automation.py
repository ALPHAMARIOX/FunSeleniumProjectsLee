from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pyttsx3
import time


def automateYouTube(searchtext):

    # Giving the path of the Chrome Driver to Selenium Webdriver
    path = "C:\\Users\\AlphaMK\\Downloads\\chromedriver"

    url = "https://www.youtube.com/"

    # Opening YouTube in the Chrome Driver
    service_obj = Service(path)
    driver = webdriver.Chrome(service=service_obj)
    driver.get(url)

    # Find the search bar using Selenium find_element function.
    driver.find_element(By.NAME, "search_query").send_keys(searchtext)

    # Clicking the search button.
    driver.find_element(By.CSS_SELECTOR, "#search-icon-legacy.ytd-searchbox").click()

    # For finding the right match search
    WebDriverWait(driver, 10).until(expected_conditions.title_contains(MyText))

    # Clicking on the match search having same as in searched query
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.ID, "img"))).click()

    # while(True):
    #    pass


speak = sr.Recognizer()
try:
    with sr.Microphone() as speaky:

        # Adjusting the energy threshold based on
        # The surrounding noise level
        speak.adjust_for_ambient_noise(speaky, duration=0.2)
        print("listening...")

        # Listening for the user's input
        searchquery = speak.listen(speaky)

        # Using Google to recognize audio
        MyText = speak.recognize_google(searchquery)
        MyText = MyText.lower()

except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

except sr.UnknownValueError:
    print("Unknown Error Occurred")

automateYouTube(MyText)