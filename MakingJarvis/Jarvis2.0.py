import random
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
import json
i = 1
dict = {"Tanuja":"juyaltanuja.01@gmail.com",
        "Manas":"mamashverma@gmail.com",
        "Mamta":"sharmamta765@gmail.com"}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[].id)
engine.setProperty('voice', voices[0].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour <= 16 :
        speak("Good Afternoon sir!")
    elif hour > 4 and hour <= 19:
        speak("Good Evening sir!")
    else:
        speak("Good night sir!")
    speak("I am Jarvis, How can i help you sir")


def speak(messsage):
    engine.say(messsage)
    engine.runAndWait()

def takeCommand():
    # It takes micorphone input input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}")

    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("parasverma0527@gmail.com", "jelbsrkbwmjmgvae")
    server.sendmail("parasverma0527@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing task based on quer
        if "wikipedia" in query:
            speak("Searching for you results...")
            # query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("you tube.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open stack overflow" in query:
            webbrowser.open("StackOverflow.com")

        elif "open google" in query:
            webbrowser.open("Google.com")

        elif "play music" in query:
            music_dir = "C:\\Users\\user\\Music\\pahadi_songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            i= i + 1

        elif "play another song" in query:
            if i != 1:
                # music_dir = "C:\\Users\\user\\Music\\pahadi_songs"
                # songs = os.listdir(music_dir)
                # print(songs)
                os.startfile(os.path.join(music_dir, random.choice(songs)))

            else:
                speak("Please play any song first after that i can change the songs for you")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir! The time is:")
            speak(strTime)
            print(f"Sir! The time is:{strTime}")

        elif "open code" in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "email to tanuja" in query:
            try:
                speak("what's your message for tanuja")
                content = takeCommand()
                to = dict["Tanuja"]
                sendEmail(to, content)
                print("Email has been sent")
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend! I am not able to sent your mail and i apologize for that")


        elif "email to Manas" in query:
            try:
                speak("what's your message for Manas")
                content = takeCommand()
                to = dict["Manas"]
                sendEmail(to, content)
                print("Email has been sent")
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend! I am not able to sent your mail and i apologize for that")

        elif "what's today's news" in query:
            r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=3671f58f31eb4c94acfb56fe503a617b")
            text = r.text
            print(r.text)
            print(r.status_code)
            myjson = json.loads(text)
            speak("Here your news for today Sir!")
            for i in range(1, 11):
                speak(f"{i} news is")
                speak(myjson['articles'][i]['title'])

        elif "open snake game" in query:
            print("The name of this game is Snake, Water, Gun.")
            print("You have to select one option form among of these three")
            speak("The name of this game is Snake, Water, Gun.")
            speak("You have to select one option form among of these three")
            i = 0
            j = 0
            c = 1
            while c <= 10:
                speak("Just say your choice from Snake, Water and Gun")
                query = takeCommand().lower()

                lst = ["Snake", "Water", "Gun"]
                choice = random.choice(lst)
                print(choice)
                if query == "snake" and choice == "Snake":
                    speak(f"Your choose {query}")
                    speak("Computer also choose snake")
                    print("try again")
                    speak("Try again")
                elif query == "snake" and choice == "Gun":
                    speak(f"Your choose {query}")
                    speak("Computer choose Gun")
                    print("Computer won")
                    speak("Computer won")
                    i = i + 1
                elif query == "snake" and choice == "Water":
                    speak(f"Your choose {query}")
                    speak("Computer choose water")
                    print("Paras won")
                    speak("Paras won")
                    j = j + 1
                elif query == "water" and choice == "Snake":
                    speak(f"Your choose {query}")
                    speak("Computer choose snake")
                    print("Computer won")
                    speak("Computer won")
                    i = i + 1
                elif query == "water" and choice == "Gun":
                    speak(f"Your choose {query}")
                    speak("Computer choose gun")
                    print("Paras won")
                    speak("Paras won")
                    j = j + 1
                elif query == "water" and choice == "Water":
                    speak(f"Your choose {query}")
                    speak("Computer choose water")
                    print("Try again")
                    speak("Try again")
                elif query == "gun" and choice == "Snake":
                    speak(f"Your choose {query}")
                    speak("Computer choose snake")
                    print("Paras won")
                    speak("Paras won")
                    j = j + 1
                elif query == "gun" and choice == "Gun":
                    speak(f"Your choose {query}")
                    speak("Computer choose gun")
                    print("Try again")
                    speak("Try again")
                elif query == "gun" and choice == "Water":
                    speak(f"Your choose {query}")
                    speak("Computer choose water")
                    print("Computer won")
                    speak("Computer won")
                    i = i + 1
                else:
                    print("Please tell me the values only snake,water,gun")
                    speak("Please tell me the values only snake,water,gun")
                c = c + 1

            if j < i:
                print("Computer won with", i, "points")
                speak(f"Computer won with {i} points")
            if i < j:
                print("Paras won with", j, "points")
                speak(f"Paras won with {j} points")

        elif "kenzie" in query:
            speak("Hey kenzie, always be happy god is always with you and can share any of your problem with my Sir")

        




