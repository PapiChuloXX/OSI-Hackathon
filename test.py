import tkinter as tk
import requests
import sunpos
from Location import time_diff
from timezonefinder import TimezoneFinder

class App:
    def __init__(self, master):
        self.master = master
        master.title("Solar Angle Calculator")

        # Address label and entry
        self.label_address = tk.Label(master, text="Enter address:", anchor="w")
        self.label_address.pack(fill="x", padx=10, pady=10)
        self.entry_address = tk.Entry(master, width=50)
        self.entry_address.pack(fill="x", padx=10)

        # Solar angle label and entry
        self.label_solar_angle = tk.Label(master, text="Enter solar angle (degrees):", anchor="w")
        self.label_solar_angle.pack(fill="x", padx=10, pady=10)
        self.entry_solar_angle = tk.Entry(master, width=10)
        self.entry_solar_angle.pack(fill="x", padx=10)

        # Calculate button
        self.button = tk.Button(master, text="Calculate", command=self.calculate)
        self.button.pack(padx=10, pady=10)

        # Result label
        self.label_result = tk.Label(master, text="", anchor="w")
        self.label_result.pack(fill="x", padx=10)

    def calculate(self):
        # Get address and solar angle from user input
        address = self.entry_address.get()
        solar_angle = self.entry_solar_angle.get()
        API_KEY = "AIzaSyAOlXE709gmbTW4gPyVGCxS33Px4pYlnGo"
        
        # Retrieve latitude and longitude using Google Maps API
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {"address": address, "key": API_KEY}
        response = requests.get(url, params=params).json()
        
        
        if response["status"] == "OK":
            lat = response["results"][0]["geometry"]["location"]["lat"]
            lng = response["results"][0]["geometry"]["location"]["lng"]
        else:
            self.label_result.config(text="Error: Could not retrieve location")
            return

        tf = TimezoneFinder()
        timezone = tf.timezone_at(lng=lng, lat=lat)
        # Display latitude and longitude in a text label
        location = (lat, lng)

        # Fourth of July, 2022 at 11:20 am MDT (-6 hours)
        when = (2023, 4, 20, 19, 33, 0, time_diff(timezone))

        azimuth, elevation = sunpos.sunpos(when, location, True)
        result = f"{azimuth}, {elevation}"
        self.label_result.config(text=result)


root = tk.Tk()
app = App(root)
root.mainloop()
