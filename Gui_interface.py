import tkinter as tk


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

        # Date and time label and entries
        self.label_date = tk.Label(master, text="Enter date (YYYY-MM-DD):", anchor="w")
        self.label_date.pack(fill="x", padx=10, pady=10)
        self.entry_year = tk.Entry(master, width=5)
        self.entry_year.pack(side="left", padx=10)
        self.label_year = tk.Label(master, text="Year", anchor="w")
        self.label_year.pack(side="left", padx=5)
        self.entry_month = tk.Entry(master, width=3)
        self.entry_month.pack(side="left")
        self.label_month = tk.Label(master, text="Month", anchor="w")
        self.label_month.pack(side="left", padx=5)
        self.entry_day = tk.Entry(master, width=3)
        self.entry_day.pack(side="left")
        self.label_day = tk.Label(master, text="Day", anchor="w")
        self.label_day.pack(side="left", padx=5)
        self.label_time = tk.Label(master, text="Enter time (HH:MM):", anchor="w")
        self.label_time.pack(fill="x", padx=10, pady=10)
        self.entry_hour = tk.Entry(master, width=3)
        self.entry_hour.pack(side="left", padx=10)
        self.label_hour = tk.Label(master, text="Hour", anchor="w")
        self.label_hour.pack(side="left", padx=5)
        self.entry_minute = tk.Entry(master, width=3)
        self.entry_minute.pack(side="left")
        self.label_minute = tk.Label(master, text="Minute", anchor="w")
        self.label_minute.pack(side="left", padx=5)

        # Calculate button
        self.button = tk.Button(master, text="Calculate", command=self.calculate)
        self.button.pack(padx=10, pady=10)

        # Result label
        self.label_result = tk.Label(master, text="", anchor="w")
        self.label_result.pack(fill="x", padx=10)

    def calculate(self):
        # Get address, solar angle, and date/time from user input
        address = self.entry_address.get()
        solar_angle = self.entry_solar_angle.get()
        year = int(self.entry_year.get())
        month = int(self.entry_month.get())
        day = int(self.entry_day.get())
        hour = int(self.entry_hour.get())

        
root = tk.Tk()
app = App(root)
root.mainloop()