import tkinter
from turtle import bgcolor
import requests
import json
import tkinter
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
rt = tkinter.Tk()
rt.geometry("500x500")
rt.config(bg='red')
frame0 = tkinter.Frame(bg='green', height=250, width=250)

label = tkinter.Label(frame0, text=data['coord'], wraplength=300)
button = tkinter.Button(frame0, width=5, height=5)
button.place(x=0, y=0)
frame0.pack()


# Displays weather

# Placements Locations
rt.mainloop()