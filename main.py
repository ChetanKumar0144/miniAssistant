from mimetypes import init
from multiprocessing.spawn import _main
import smtplib
from tkinter import EXCEPTION
from pip import main
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtpd

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')

# print(voices[1].id)

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good after noon")
    else:
        speak("good evening")
    
    speak("Hello Chetan, I am your assistant. How I help You?")

def take_command():
    # it takes microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    
    except Exception as e:
        print(e)

        print("Say that again")
        return "none"
    
    return query

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chetankumar0144@gmail.com','Chetan@3011')
    server.sendmail('chetankumar0144@gmail.com',to,content)
    server.close

if __name__ =="__main__":
    wishme()
    # while True:
    if 1:
        query = take_command().lower()
        # logic for executing task based on query 
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query , sentences=2)
            speak("According To wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")
 
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = 'D:\\btech\\work'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime} ")
        elif 'open code' in query:
            path = "C:\\Users\\Avita Liber V\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'email to chetan' in query:
            try:
                speak("what should I say?")
                content = take_command()
                to = "chinusohlot@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except EXCEPTION as e:
                print(e)
                speak("Sorry sir, Email is not sent")