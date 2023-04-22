import tkinter as tk
import requests
from GlobalIrraddiance import global_irridance

class App:
    def __init__(self, master):
        self.master = master
        master.title("Solar Angle Calculator")

        # Address label and entry
        self.label_address = tk.Label(master, text="Enter address:", anchor="w")
        self.label_address.pack(fill="x", padx=10, pady=10)
        self.entry_address = tk.Entry(master, width=50)
        self.entry_address.pack(fill="x", padx=10)


        # area of solar panel label and entry
        self.label_solar_area = tk.Label(master, text="Enter number of solar panels:", anchor="w")
        self.label_solar_area.pack(fill="x", padx=10, pady=10)
        self.entry_solar_area = tk.Entry(master, width=10)
        self.entry_solar_area.pack(fill="x", padx=10)

        # Calculate button
        self.button = tk.Button(master, text="Calculate", command=self.calculate)
        self.button.pack(padx=10, pady=10)

        # Result label
        self.result_text = tk.StringVar()
        self.label_result = tk.Label(master, text="", anchor="w")
        self.label_result.pack(fill="x", padx=10)

    def calculate(self):
        # Get address and solar angle from user input
        self.result_text.set('')
        address = self.entry_address.get()
        number = float(self.entry_solar_area.get())
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


        Energy = global_irridance(lat,lng) * number
        result = f"Your total energy for one day : {Energy/1000}KW"
        self.label_result.config(text=result)

        

root = tk.Tk()
app = App(root)
root.mainloop()
