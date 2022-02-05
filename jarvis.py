import datetime
import os
import smtplib
import webbrowser
from pandas import factorize
import pyttsx3
import speech_recognition as sr
import wikipedia
from geopy.geocoders import Nominatim

from bs4 import BeautifulSoup

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
rate=engine.getProperty('rate')
engine.setProperty('rate',150)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<6:
        speak("Good Afternoon!")

    else :
        speak("Good Evening!")
    
    speak("I am Jarvis,Please tell me how may i hep you")       


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=.6
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query} \n")
    
    except Exception as e:
        print("Say again please...")
        return "None"
    speak(f"You asked for {query}")
    return query    


def get_coordinates(address_):
     # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")

    try: 
        getLoc = loc.geocode(address_)
 
        print(getLoc.address)
        
        co_ordinate="Latitude="+str(getLoc.latitude)+"Longitude="+str(getLoc.longitude)
        speak()

        print(co_ordinate)

    except Exception as e:
        speak("Please give your location again")  
        address=takeCommand().lower()
        get_coordinates(address)  

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
if __name__== "__main__":
    wishMe()
    while 1:
        query=takeCommand().lower()
        
        if "jarvis who are you" in query:
            speak("Hello sir,I am jarvis version 2.0 I was made by Neel")
        
        elif 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=5)
            speak("According to Wikkipedia")
            print(results)
            speak(results)
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        # elif 'play music' in query:
        #     music_dir=''
        #     songs=os.listdir(music_dir)
        #     os.startfile(os.path.join(music_dir,songs[0]))        
        
        elif 'vs code' in query:
            vscode_dir='C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk'
            os.startfile(vscode_dir)        
      
        elif 'open pushpa' in query:
            pushpa_dir='D:\\Pushpa 720p ethmovies.xyz.mkv'
            os.startfile(pushpa_dir)        

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is{strTime}")
        
        elif "my co-ordinate" in query:
            speak("what is your location?")
            address=takeCommand().lower()
            get_coordinates(address)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "20BCS091@iiitdwd.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
        
        elif 'open facebook' in query:
            try:
                from googlesearch import search
            except:
                speak("Failed to import Google Search")    
            
            query_1='facebook'
            for j in search(query, tld="co.in", num=1, stop=1):
                webbrowser.open(j)
         
        elif 'open github' in query:
            webbrowser.open("https://github.com/neel-yad") 

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")


        else:
            speak("Sorry I cant recognise,Please speak again")



