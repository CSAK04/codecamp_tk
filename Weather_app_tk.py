from tkinter import *
import sqlite3
import json
import requests

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=8624A25A-471F-451A-A11F-250182444D5B

a = Tk()


def zip_lookout():
    global lab

    try:
        lab.grid_forget()

        request_api = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip_entry.get()+"&distance=25&API_KEY=8624A25A-471F-451A-A11F-250182444D5B")
        api_full = json.loads(request_api.content)

        api = api_full[0]
        print(api)
        area = api["ReportingArea"]
        latitude = api["Latitude"]
        condition = api["Category"]["Name"]

        if condition == "Good":
            color = "#00E400"
        elif condition == "Moderate":
            color = "#ffff00"
        elif condition == "Unhealthy for Sensitive Groups":
            color = "#ff7e00"
        elif condition == "Unhealthy":
            color = "#ff0000"
        elif condition == "Very Unhealthy":
            color = "#99004c"
        else:
            color = "#7e0023"

        lab = Label(text="Zip code:"+zip_entry.get()+"\n"+"Air Quality Index (AQI) : " + str(api['AQI']) + "\n" +
                         "Reporting Area: " + area + "\n" + "Condition: " + condition, font=("helvatica", 20), bg=color)
        lab.grid(row=5, column=0, columnspan=2)

        a.configure(background=color)

    except Exception as e:
        api_full = "Error"


zip_entry = Entry()
zip_entry.grid(row=0, column=0, pady=(10, 10), padx=(10, 10), sticky=W+E+N+S)

lab = Label(text="", font=("helvatica", 20))
lab.grid(row=5, column=0, columnspan=2)

lab.grid_forget()

zip_btn = Button(text="check for this zipcode", command=zip_lookout)
zip_btn.grid(row=0, column=1, pady=(10, 10), padx=(10, 10), sticky=W+E+N+S)

a.mainloop()
