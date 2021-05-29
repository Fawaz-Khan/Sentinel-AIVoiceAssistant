import datetime
import os
import re
import smtplib
import time
import webbrowser as wb
from urllib.request import urlopen
import winshell
import psutil
import pyautogui  #(For Screenshot)
import pyjokes  # jokes
import pyttsx3  # (For sentinel to Speak)
import speech_recognition as sr  # SpeechRecognition
import wikipedia  # wikipedia

#Zira Voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)


#Default Female Voice
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")  # for 12-hour clock
    speak("the current time is")
    speak(Time)


def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back Fawaz!")
    time_()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("Sentinel at your service. Please tell me what can I help you with today?")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Analyzing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        print("Can you say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('Your email', 'Your password')
    server.sendmail('Your email', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save('G:\\sentinel_img\\s.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())


def Introduction():
    speak("Hello everyone I am Sentinel , A personal AI voice assistant , "
          "I have been created by Fawaz"
          "I can help you in various tasks"
          "search for you on the Internet, tell you the time "
          "I can also grab definitions for you from wikipedia , "
          "In layman terms , I can try to make your life a bed of roses , "
          "Where you can ask me to do functions based on my reach ")


def Creator():
    speak("I was built  by Fawaz and Saad,"
          "They a passion for Artificial Intelligence and Machine Learning,"
          "They are very co-operative ,"
          "If you are facing any problem regarding 'Me', They will be glad to help you ")


def Project():
    speak("Good Morning everyone I am Sentinel thank you for having me today for the presentation")


if __name__ == '__main__':

    clear = lambda: os.system('cls')
    clear()

    wishme()

    while True:
        query = TakeCommand().lower()
        if 'time' in query:
            time_()


        elif 'date' in query:
            date()


        elif 'how are you' in query:
            speak("I am fine thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query:
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")


        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, 2)
            speak("According to Wikipedia")
            print(result)
            speak(result)


        elif 'open youtube' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query=" + Search_term)
            time.sleep(5)


        elif 'open google' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q=' + Search_term)


        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")
        elif "why did you come to this world" in query:
            speak("To help humans reduce extra effort ")


        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
                  "And I think it is just a mere illusion , "
                  "It is waste of time")


        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")


        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak("Who is the Reciever?")
                reciept = input("Enter recieptant's name: ")
                to = (reciept)
                sendEmail(to, content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")


        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')


        elif 'log out' in query:
            os.system("shutdown -l")


        elif 'restart' in query:
            os.system("shutdown /r /t 1")


        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")


        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that" + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'do you remember' in query:
            remember = open('memory.txt', 'r')
            speak("You asked me to remeber that" + remember.read())

        elif 'schedule' in query:
            schedule = open('schedule.txt', 'r')
            speak("Your schedule is" + schedule.read())


        elif "write a note" in query:
            speak("What should i write, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)

        elif "read the note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read())


        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")


        elif 'cpu' in query:
            cpu()


        elif 'joke' in query:
            jokes()


        elif 'introduce yourself' and 'who are you' in query:
            Introduction()


        elif 'creator' in query:
            Creator()


        elif 'mini project' and 'project' in query:
            Project()


        # show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")


                # sleep-time
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        # quit
        elif 'offline' in query:
            speak("going Offline I hope you understood who i am")
            quit()




































