import requests
import pyttsx3
import json

city = input("Enter you city : ")
url = f"YOUR_API"
r = requests.get(url)

wdic = json.loads(r.text)
w = wdic["current"] ["temp_c"]
print(w)
engine = pyttsx3.init()
engine.say(f"The current weather in {city} is {w} degrees")
engine.runAndWait()

