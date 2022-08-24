from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import speech_recognition as sr


def VoiceGoogle(searchtext):
    service_obj = Service('C:\\Users\\AlphaMK\\Downloads\\chromedriver')
    driver = webdriver.Chrome(service=service_obj)

    driver.get("https://google.ca/search?q=" + searchtext)

    #while True:
        #pass


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

VoiceGoogle(MyText)