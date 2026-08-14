import time
import pyttsx3
import speech_recognition as sr

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
    speak("I am ready for your command, doctor.")

if __name__ == "__main__":
    speak("Tinkle system initialized.")
    while True:
        listen_for_trigger()
