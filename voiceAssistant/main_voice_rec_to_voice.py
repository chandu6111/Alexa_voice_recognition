import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

engine.say('Hey Chandu, I am your voice assistant Alexa')
engine.say('How can I help you?')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("How can I help you? ")
            audio = r.listen(source)
            print("done!")
            ch = r.recognize_google(audio).lower()
            print("You said : "+ ch)
            return ch
    except Exception as e:
        print(e)

while True:
    ch=take_command()
    if "play" in ch:
        song=ch.replace('play','')
        talk('playing a beautiful song for you dear')
        pywhatkit.playonyt(song)
    elif "time" in ch:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is: '+time)
    elif "who is" in ch:
        person=ch.replace('who is','')
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif "joke" in ch:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif(("notepad" in ch or "editor" in ch or "text editor" in ch or "write" in ch ) and ("not" not in ch)):
        talk("Opening Notepad")
        os.system('"notepad.exe"')
    elif(("browse" in ch or "google" in ch or "search" in ch or "chrome" in ch or "net" in ch or "internet" in ch) and ("not" not in ch)):
        talk("Opening Chrome")
        webbrowser.open("google.com")
    elif(("message" in ch or "whatsapp" in ch or "text" in ch or "ping" in ch or "call" in ch) and ("not" not in ch)):
        talk("Opening Whatsapp")
        webbrowser.open("whatsapp.com")
    elif(("youtube" in ch or "you tube" in ch)  and ("not" not in ch) ):
        talk("Opening you tube")
        webbrowser.open("youtube.com")
    elif("twitter" in ch  and ("not" not in ch)):
        talk("Opening Twitter")
        webbrowser.open("twitter.com")
    elif("facebook" in ch  and ("not" not in ch)):
        talk("Opening Facebook")
        webbrowser.open("facebook.com")
    elif("linkedin" in ch  and ("not" not in ch)):
        talk("Opening Linkedin")
        webbrowser.open("linkedin.com")
    elif("mail" in ch  and ("not" not in ch)):
        talk("Opening Gmail")
        webbrowser.open("gmail.com")
    elif(("calculate" in ch or "calculator" in ch or "calculations" in ch) and ("not" not in ch)):
        talk("Opening Calculator")
        os.system("calc.exe")
    elif(("paint" in ch or "draw" in ch or "sketch" in ch) and ("not" not in ch)):
        talk("Opening Paint")
        os.system("mspaint.exe")
    elif("thank" in ch):
        talk("You are welcome")
        print("You are welcome :)")
    elif("help" in ch):
        talk("I can open Notepad , Google , You tube , Gmail , Linkedin , Facebook , Twitter ,  Calculator , Paint , Whatsapp, wikipedia, play a song, tell the time, crack a joke")
        print("Notepad")
        print("Google")
        print("You Tube")
        print("Gmail")
        print("Linkedin")
        print("Facebook")
        print("Twitter")
        print("Calculator")
        print("Paint")
        print("Whatsapp")   
    elif("do not" in ch):
        print("Okay!")
        talk("Fine")
    elif("stop" in ch or "get lost" in ch):
        talk("Thank you , Have a nice day")
        print("Thank you , Have a Nice day !")
        break
    else:
        talk("Sorry, I could not understand. Once type help to see whether the command is there or not ")
        print("Sorry, I could not understand. Once type help to see whether the command is there or not")    
    talk("How else can I help you dear?")
