import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')  
engine.setProperty('rate', rate - 50)

recognizer = sr.Recognizer()

def voice():
    with sr.Microphone() as source:
        print('wait')
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print("Say something...")
        speech('tell')
        try:
            audio = recognizer.listen(source)
            print('v')
            text = recognizer.recognize_google(audio)
            print('rec:'+text)
            return text
        except:
            print('re-try>>>')
            speech('re try')
            return voice()

def speech(text):   
    engine.say(text)
    engine.runAndWait()

