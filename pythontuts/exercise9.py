# def speak(str):
#     from win32com.client import Dispatch
#
#     speak = Dispatch("SAPI.SpVoice")
#
#     speak.speak(str)
# speak("Sorry tannu . I will never do this again, Dost nahi hai maaf karde yaarr ")


def speak(str):
    spea = Dispatch("SAPI.spvoice")
    print(str)
    spea.speak(str)

import requests
import json
from win32com.client import Dispatch
r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=3671f58f31eb4c94acfb56fe503a617b")
text=r.text
print(r.text)
print(r.status_code)
myjson = json.loads(text)
speak("Good Afternoon Mamta! Here your news for todays!")
for i in range(1, 11):
    speak(f"{i} news is")
    speak(myjson['articles'][i]['title'])



