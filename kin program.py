import pyttsx3
#import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#wishes according to time
def wiseMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")

    else:
        speak("good evening! sir")

    speak("i am kin!, please tell me how may i help u sir")



#add name
def name(name):
    if len(name) < 4:
         speak("Please enter a valid name sir")
    elif len(name) > 5:
        speak("Sir your name is " + (name))
        print("Sir your name is " + (name))
        speak ("Valid username sir , thank you for adding your name")

#kin info(program info)
def aboutukin():
    speak("I'm a speaking program made by Nitish , i'm coded by python language, hope u will enjoy using me")

#creator info
def creator():
    speak("Niitish is the creator of kin program")

if __name__ == "__main__":
    wiseMe()
    aboutukin()
    name()

    speak("hello world!")
