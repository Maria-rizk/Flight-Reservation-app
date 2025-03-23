import tkinter as tk
from tkinter import messagebox
import sqlite3

class EditReservationPage:
    def __init__(self, root, reservations_root, reservation_id):
        self.root = root
        self.reservations_root = reservations_root
        self.reservation_id = reservation_id
        self.root.title("Edit Reservation")
        self.root.geometry("400x300")

        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute("SELECT * FROM reservations WHERE id=?", (reservation_id,))
        reservation = c.fetchone()
        conn.close()

        tk.Label(root, text="Edit Reservation", font=("Arial", 14)).pack(pady=10)

        self.name = tk.Entry(root, width=30)
        self.name.insert(0, reservation[1])
        self.name.pack(pady=5)

        self.flight_number = tk.Entry(root, width=30)
        self.flight_number.insert(0, reservation[2])
        self.flight_number.pack(pady=5)

        self.departure = tk.Entry(root, width=30)
        self.departure.insert(0, reservation[3])
        self.departure.pack(pady=5)

        self.destination = tk.Entry(root, width=30)
        self.destination.insert(0, reservation[4])
        self.destination.pack(pady=5)

        self.date = tk.Entry(root, width=30)
        self.date.insert(0, reservation[5])
        self.date.pack(pady=5)

        self.seat_number = tk.Entry(root, width=30)
        self.seat_number.insert(0, reservation[6])
        self.seat_number.pack(pady=5)

        tk.Button(root, text="Update", command=self.update_reservation, width=20).pack(pady=10)
        tk.Button(root, text="Back", command=self.go_back, width=20).pack(pady=10)

    def update_reservation(self):
        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute("UPDATE reservations SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=? WHERE id=?",
                  (self.name.get(), self.flight_number.get(), self.departure.get(), self.destination.get(), self.date.get(), self.seat_number.get(), self.reservation_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation updated!")
        self.go_back()

    def go_back(self):
        self.root.destroy()
        self.reservations_root.deiconify()