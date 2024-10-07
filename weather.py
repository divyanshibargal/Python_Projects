import requests
import pyttsx3
import json

city = input("Enter you city : ")
url = f"http://api.weatherapi.com/v1/current.json?key=b31d96b248eb48e8a46125730240406&q={city}&aqi=no"
r = requests.get(url)

wdic = json.loads(r.text)
w = wdic["current"] ["temp_c"]
print(w)
engine = pyttsx3.init()
engine.say(f"The current weather in {city} is {w} degrees")
engine.runAndWait()

