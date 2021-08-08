import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am jarvis Sir. Please tell me how may i help you")


def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        Query = r.recognize_google(audio, language='en-in')
        print("User said: ", Query)
    except Exception as e:
        # print(e)
        print("say that again please...")
        speak("sir,say that again please...")
        return "None"
    return Query


if __name__ == '__main__':
    wishme()
    while True:
        Query = takeCommand().lower()
        # logics for executing tasks based on Query
        if 'wikipedia' in Query:                
            speak("Searching wikipedia....")
            Query = Query.replace("wikipedia", "")
            results = wikipedia.summary(Query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in Query:
            webbrowser.open("youtube.com")

        elif 'open google' in Query:
            webbrowser.open("google.com")

        elif 'shutdown' in Query:
            print("jarvis is shutting down....")
            speak("jarvis is shutting down....")
            exit()

        elif 'time' in Query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strTime}")
            print(strTime)

        elif 'play music' in Query:
            music_dir = 'v:\\music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open code' in Query:
            code_path = "C:\\Users\\vanam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("visual studio code is opening....")
            os.startfile(code_path)
            exit()
            