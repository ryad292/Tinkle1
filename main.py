import time
import pyttsx3
import speech_recognition as sr
from skills import TinkleSkills

# تهيئة محرك الصوت
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print(f"Tinkle: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_for_trigger():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tinkle is listening for 'Tinkle'...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            command = recognizer.recognize_google(audio, language="en-US").lower()
            
            if "tinkle" in command:
                speak("Yes, doctor.")
                active_mode()
        except Exception as e:
            pass

def active_mode():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening for your command, doctor.")
        try:
            audio = recognizer.listen(source, timeout=6, phrase_time_limit=5)
            command = recognizer.recognize_google(audio, language="en-US")
            print(f"Command received: {command}")
            TinkleSkills.execute(command, speak)
        except Exception as e:
            speak("I didn't catch that, doctor.")

if __name__ == "__main__":
    speak("Tinkle system initialized.")
    while True:
        listen_for_trigger()
