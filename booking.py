import tkinter as tk
from tkinter import messagebox
import sqlite3

class BookingPage:
    def __init__(self, root, home_root):
        self.root = root
        self.home_root = home_root
        self.root.title("Book Flight")
        self.root.geometry("400x300")

        tk.Label(root, text="Book a Flight", font=("Arial", 14)).pack(pady=10)

        self.name = tk.Entry(root, width=30)
        self.name.insert(0, "Name")
        self.name.pack(pady=5)

        self.flight_number = tk.Entry(root, width=30)
        self.flight_number.insert(0, "Flight Number")
        self.flight_number.pack(pady=5)

        self.departure = tk.Entry(root, width=30)
        self.departure.insert(0, "Departure")
        self.departure.pack(pady=5)

        self.destination = tk.Entry(root, width=30)
        self.destination.insert(0, "Destination")
        self.destination.pack(pady=5)

        self.date = tk.Entry(root, width=30)
        self.date.insert(0, "Date (YYYY-MM-DD)")
        self.date.pack(pady=5)

        self.seat_number = tk.Entry(root, width=30)
        self.seat_number.insert(0, "Seat Number")
        self.seat_number.pack(pady=5)

        tk.Button(root, text="Submit", command=self.save_reservation, width=20).pack(pady=10)
        tk.Button(root, text="Back", command=self.go_back, width=20).pack(pady=10)

    def save_reservation(self):
        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute("INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number) VALUES (?, ?, ?, ?, ?, ?)",
                  (self.name.get(), self.flight_number.get(), self.departure.get(), self.destination.get(), self.date.get(), self.seat_number.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation saved!")
        self.go_back()

    def go_back(self):
        self.root.destroy()
        self.home_root.deiconify()