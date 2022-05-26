import tkinter
import requests
import json
from tkinter import *
from pprint import pprint

API_KEY = 'bc50760d54528b10f34315f689817b3c'

#city = input("Enter a city: ")
# Grabbing weather data
city = "Boston"

base_url =  "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

weather_data = requests.get(base_url).json()

#pprint(weather_data)
# Grabbing the json dump from weather api
dataDump = json.dumps(weather_data)
data = json.loads(dataDump)
pprint(data)

images = [[],[],[],[],[],[]]

# tkinter windows
rt = Tk()
label = Label(rt, text=data, wraplength=300)
label.pack()

rt.mainloop()