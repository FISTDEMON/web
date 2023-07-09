import time
import speech_recognition as sr
import pyttsx3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to get voice command from the user
def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm unable to process your request at the moment.")
        return ""


# Function to speak the response
def speak(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()


# Greet the user
speak("Hello! How can I assist you today?")

# Create a new instance of the ChromeDriver service
service = Service("C:\\ProgramData\\chocolatey\\lib\\chromedriver\\tools\\chromedriver.exe")
service.start()

# Create a new instance of the Chrome WebDriver with the service
driver = webdriver.Chrome(service=service)

# Main program loop
while True:
    command = get_voice_command()
    if command:
        if "open google" in command:
            speak("Google opened in Chrome browser.")
            driver.get('https://www.google.com')

        elif "search amazon" in command:
            speak("What would you like to search on Amazon?")
            search_query = get_voice_command()
            speak(f"Searching Amazon for '{search_query}'")
            driver.get(f'https://www.amazon.com/s?k={search_query}')

        elif "open amazon" in command:
            speak("Opening Amazon.")
            driver.get('https://www.amazon.com')

        elif "scroll down" in command:
            speak("Scrolling down the page.")
            scroll_height = 0
            while scroll_height < 1000:
                scroll_height += 50
                driver.execute_script("window.scrollTo(0, " + str(scroll_height) + ");")
                time.sleep(0.5)

        elif "scroll up" in command:
            speak("Scrolling up the page.")
            scroll_height = 1000
            while scroll_height > 0:
                scroll_height -= 50
                driver.execute_script("window.scrollTo(0, " + str(scroll_height) + ");")
                time.sleep(0.5)

        elif "search batman".lower() in command.lower():
            speak("Searching for Batman.")
            driver.get('https://en.wikipedia.org/wiki/Batman')

        elif "click on first link" in command.lower():
            speak("Clicking on the first link.")
            first_link = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')))
            first_link.click()

        elif "exit from the browser" in command:
            speak("Closing the browser. Goodbye!")
            break

# Close the browser window and stop the ChromeDriver service
driver.quit()
service.stop()











