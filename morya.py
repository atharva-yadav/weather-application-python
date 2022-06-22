# Weather Application using API

# importing the libraries
from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image

# necessary details
root = Tk()
root.title("Weather App")
root.geometry("890x495")
root.resizable(False, False)
root.wm_iconbitmap("Weather.ico")
root['background'] = "white"


image = Image.open('Weather (Custom).png')
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo, bg="#4a536b")
label.grid(row=1)


# Dates
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A'), bg="#f3ad19", font="poppins 10")
date.place(x=700, y=440)
month = Label(root, text=dt.strftime('%d %B %Y'), bg="#f3ad19", fg="White", font="Poppins 10 bold")
month.place(x=790, y=440)

Label(root, text="Current time: ", bg="#f3ad19", font="Poppins 10").place(x=700, y=460)
# Time
hour = Label(root,
             text=dt.strftime("%H:%M:%S"),
             bg='#f3ad19',
             fg="White",
             font="Poppins 10 bold")
hour.place(x=790, y=460)


# City Search
city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=25, font="Poppins 12")
city_entry.place(x=120, y=10)



# -------------------------------------------------------------------------------------------

def city_name():

    # API Call
    api_request = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" +
        city_entry.get() + "&units=metric&appid=" + "407dc0396b20a0ebbd36ae06e6b741ba")

    print(api_request)

    if(api_request == "<Response [404]>"):
        lable_citi.configure(text="City Not Found")
        return

    print(api_request.content)
    api = json.loads(api_request.content)

    # Temperatures
    y = api['main']
    current_temprature = y['temp']
    humidity = y['humidity']
    tempmin = y['temp_min']
    tempmax = y['temp_max']
    pressure = y['pressure']

    # Coordinates
    # x = api['coord']
    # longtitude = x['lon']
    # latitude = x['lat']

    # Weather
    p = api['weather']
    status = p[0]['description']
    print(status)

    # Country
    z = api['sys']
    country = z['country']
    citi = api['name']

    # Wind
    q = api['wind']
    windspeed = q['speed']
    print(windspeed)
    

    # Adding the received info into the screen
    lable_temp.configure(text=current_temprature)
    lable_humidity.configure(text=humidity)
    min_temp.configure(text=tempmin)
    max_temp.configure(text=tempmax)
    lable_pressure.configure(text=pressure)
    lable_status.configure(text=status)
    lable_country.configure(text=country)
    lable_citi.configure(text=citi)
    lable_windspeed.configure(text=windspeed)

# -------------------------------------------------------------------------------------------

Label(root, text="Enter your city: ", font="Poppins 10", bg="#eccc2b").place(x=10, y=11)

# Search Bar and Button - function will get executed after presing button
city_nameButton = Button(root, text="Get Weather", command=city_name, width=15, bg="white", height=1, cursor="arrow", font="Poppins 10 ")
city_nameButton.place(x=400, y=10)

# Country Names and Coordinates
lable_citi = Label(root, text="", width=0, bg='#ebc92a', font="Montserrat 30 bold")
lable_citi.place(x=20, y=50)

lable_country = Label(root, text="", width=0, bg='#ebc92a', font="Montserrat 30 bold")
lable_country.place(x=195, y=50)

lable_status = Label(root, text="", width=0, bg='#ebc92a', font="Montserrat 10")
lable_status.place(x=20, y=100)

# Current Temperature
Label(root, text="Current Temperature: ", font="Montserrat 15 bold", fg="Orange", bg="white").place(x=20, y=150)
lable_temp = Label(root, text="...", width=0, bg='white', font="Montserrat 100", fg='black')
lable_temp.place(x=20, y=180)

# Other temperature details
Label(root, text="______________________________________", font="Montserrat 15 bold", height=1 ,fg="red", bg="white").place(x=500, y=160)
Label(root, text="Other Details: ", font="Montserrat 15 bold", fg="Orange", bg="white").place(x=500, y=150)

# Humidity
humi = Label(root, text="Humidity: ", width=0, bg='white', font="Poppins 15 ")
humi.place(x=550, y=200)

lable_humidity = Label(root, text="", width=0, bg='#ecc82a', font="Montserrat 15 ")
lable_humidity.place(x=670, y=200)

# Maximum temperature
maxi = Label(root, text="Max. Temperature:", width=0, bg='white', font="Poppins 15 ")
maxi.place(x=550, y=230)

max_temp = Label(root, text="", width=0, bg='#ecc82a', font="Montserrat 15 ")
max_temp.place(x=750, y=230)

# Minimum temperature
mini = Label(root, text="Min. Temperature:", width=0, bg='white', font="Poppins 15 ")
mini.place(x=550, y=260)

min_temp = Label(root, text="", width=0, bg='#ecc82a', font="Montserrat 15 ")
min_temp.place(x=750, y=260)

# Pressure
pres = Label(root, text="Pressure: ", width=0, bg='white', font="Poppins 15 ")
pres.place(x=550, y=290)

lable_pressure = Label(root, text="", width=0, bg='#ecc82a', font="Montserrat 15 ")
lable_pressure.place(x=650, y=290)

# Windspeed
pres = Label(root, text="Wind Speed: ", width=0, bg='white', font="Poppins 15 ")
pres.place(x=550, y=320)

lable_windspeed = Label(root, text="..", width=0, bg='#ecc82a', font="Montserrat 15 ")
lable_windspeed.place(x=710, y=320)


# Caution
note = Label(root, text="Note: All temperatures are in Degree Celsius", bg='white', font="Poppins 10")
note.place(x=25, y=400)

# Caution
credit = Label(root, text="© Atharva Yadav - All rights reserved", bg='#edc628',fg="white", font="Poppins 10 bold")
credit.place(x=100, y=450)


root.mainloop()
