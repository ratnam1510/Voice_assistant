from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess


def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("speech.mp3")
    playsound("speech.mp3")
    os.remove("speech.mp3")


def take_comm():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print("User said: " + query + "\n")
        except Exception as e:
            print(e)
            speak("I didn't understand")
            return "None"
        return query


if __name__ == "__main__":
    speak("Jeopardize assistance activated")
    speak("How can I help you")
    while True:
        query = take_comm().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "are you" in query:
            speak("I am Jeopardize developed by Ratnam Shah")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open github" in query:
            speak("Opening GitHub")
            webbrowser.open("https://github.com")

        elif "open chatgpt" in query:
            speak("Opening ChatGPT")
            webbrowser.open("https://chat.openai.com/")

        elif "open spotify" in query:
            speak("Opening Spotify")
            subprocess.call(["open", "/Applications/Spotify.app"])

        elif "open whatsapp" in query:
            speak("Opening WhatsApp")
            subprocess.call(["open", "/Applications/WhatsApp.localized/WhatsApp.app"])

        elif "bye" in query:
            speak("Thank You and Goodbye")
            exit(1)
