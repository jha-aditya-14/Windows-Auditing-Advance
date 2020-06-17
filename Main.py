import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import smtplib
import os

print("Initializing Jarvis")

MASTER = "Aditya"

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):

    engine.say(text)
    engine.runAndWait()
speak("Initializing Jarvis...")


# This will wish me with timw
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=3 and hour <12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour<16:
        speak("Good Afternoon" + MASTER)
    elif hour>=16 and hour<20:
        speak("Good Evening" + MASTER)
    else:
        speak("Is Late Night" + MASTER)
    speak("I am Jarvis. How may I help you?")


#Main Program
def takeCommand(): # take commands from microphone
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening......")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query= r.recognize_google(audio, language = 'en-in')
        print(f"user said:{query}\n")
        
    except Exception as e:
        print("Say that again please")
        query=None
    return query.lower()



speak("Initializing Jarvis...")
wishMe()
query = takeCommand()

#Logic for executing basic task as per the query
if 'wikipedia' in query.lower():
    speak('Searching wikipedia....')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences = 2)
    speak(results)

elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")
    url = "youtube.com"
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir="C:\\Program Files (x86)\\Google\\Chrome\\"
    songs=os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir,songs[0]))

elif 'open youtube' in query.lower():
    strTime = datetime.datetime.now.strftime("%H:%M:%S")
    speak(MASTER+f"the time is {strTime}")
    


