import tkinter as tk
from booking import BookingPage
from reservations import ReservationsPage

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Reservation System")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")  # Set background color for the window

        # Header Label
        header_label = tk.Label(
            root,
            text="Flight Reservation System",
            font=("Arial", 18, "bold"),
            bg="#462255",
            fg="white",
            padx=10,
            pady=10
        )
        header_label.pack(fill=tk.X)

        # Main Frame for Buttons
        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(expand=True, pady=20)

        # Book Flight Button
        book_button = tk.Button(
            main_frame,
            text="Book Flight",
            command=self.open_booking,
            font=("Arial", 12),
            bg="#aa4465",
            fg="white",
            width=20,
            height=2,
            relief=tk.FLAT,
            activebackground="#007B9E"
        )
        book_button.pack(pady=10)

        # View Reservations Button
        reservations_button = tk.Button(
            main_frame,
            text="View Reservations",
            command=self.open_reservations,
            font=("Arial", 12),
            bg="#aa4465",
            fg="white",
            width=20,
            height=2,
            relief=tk.FLAT,
            activebackground="#007B9E"
        )
        reservations_button.pack(pady=10)

        # Footer Label
        footer_label = tk.Label(
            root,
            text="© 2023 Flight Reservation System. All rights reserved.",
            font=("Arial", 10),
            bg="#333",
            fg="white",
            pady=5
        )
        footer_label.pack(side=tk.BOTTOM, fill=tk.X)

    def open_booking(self):
        """Open the Booking Page in a new window."""
        self.root.withdraw()  # Hide the main window
        booking_window = tk.Toplevel()
        booking_window.title("Book Flight")
        booking_window.geometry("400x300")
        BookingPage(booking_window, self.root)  # Pass the main window for reopening

    def open_reservations(self):
        """Open the Reservations Page in a new window."""
        self.root.withdraw()  # Hide the main window
        reservations_window = tk.Toplevel()
        reservations_window.title("View Reservations")
        reservations_window.geometry("400x300")
        ReservationsPage(reservations_window, self.root)  # Pass the main window for reopening