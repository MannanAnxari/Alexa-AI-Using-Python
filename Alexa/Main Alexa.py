import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak Function


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Wish Me Function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello I am Alexa Sir. Please tell me how may I help you")


# Take Command From User Function
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 8000
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-uk')
        print(f"User said: {query}\n")

    except:
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':

    wishMe()
    while True:
        query = takeCommand().lower()

        # Wikipedia
        if "wikipedia" in query:
            print("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)

        # Social Links
        elif "open youtube" in query:
            url = 'http://youtube.com'
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)

        elif "open google" in query:
            url = 'http://google.com'
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)

        elif "open facebook" in query:
            url = 'http://facebook.com'
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)

        elif "play music" in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            rand = random.randint(1, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[rand]))
            break

        elif "time" in query:
            strTime = datetime.datetime.now().strftime('%H : %M : %S')
            speak(f'Sir, The Time is {strTime}')

        elif 'open code' in query:
            codePath = 'C:\\Users\\manna\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'open game' in query:
            codePath = 'G:\\Python\\Snake Game\\snk.py'
            os.startfile(codePath)

        elif 'search on youtube' in query:
            ls = []
            query = query.replace("search on youtube ", "")
            query = query.replace(" ", "+")
            # for item in query:
            #     ls.append(item + "+")
            #     print(ls)
            #        for i in ls:
            url = f"https://www.youtube.com/results?search_query={query}"
            print(query)
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)

        elif 'search on google' in query:
            query = query.replace("search on google ", "")
            url = f"https://www.google.com/search?q={query}&rlz=1C1BNSD_enPK958PK958&sxsrf=ALeKk01UUzlnPEt6HXWaaWBzh1asa6HQDQ%3A1627463255520&ei=Vx4BYdelH9O81fAPgYS04AY&oq={query}&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGABQrxJYrxJg0BdoAHACeACAAbwIiAG8CJIBAzctMZgBAKABAcABAQ&sclient=gws-wiz&ved=0ahUKEwiXreuJtYXyAhVTXhUIHQECDWwQ4dUDCA8&uact=5"
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)

        # Basics
        elif "how are you" in query:
            speak("i'm fine sir")

        elif "thanks" in query:
            speak("You'r Welcome sir.")

        # Exit Func
        elif "exit" in query:
            print("Alexa Are Quitting...\n")
            speak("Alexa Are Quitting...\n")
            time.sleep(2)
            break
