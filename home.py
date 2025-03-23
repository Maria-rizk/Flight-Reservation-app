import tkinter as tk
from booking import BookingPage
from reservations import ReservationsPage

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Reservation System")
        self.root.geometry("400x300")

        tk.Label(root, text="Flight Reservation System", font=("Arial", 16)).pack(pady=20)

        tk.Button(root, text="Book Flight", command=self.open_booking, width=20).pack(pady=10)
        tk.Button(root, text="View Reservations", command=self.open_reservations, width=20).pack(pady=10)

    def open_booking(self):
        self.root.withdraw()
        booking_window = tk.Toplevel()
        BookingPage(booking_window, self.root)

    def open_reservations(self):
        self.root.withdraw()
        reservations_window = tk.Toplevel()
        ReservationsPage(reservations_window, self.root)