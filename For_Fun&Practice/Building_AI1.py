import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia 
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print('You said: '+ command)
            return command
    except Exception as e:
        print('Could not understand audio:"', e)
        return ""
    
def run_assistant():
    command = take_command()
    if command:
        talk('You said: ' + command)

if __name__ == "__main__":
    talk('Assistant initialized.')
    run_assistant()