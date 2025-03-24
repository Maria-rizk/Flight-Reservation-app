import tkinter as tk
from tkinter import messagebox
import sqlite3

class BookingPage:
    def __init__(self, root, home_root):
        self.root = root
        self.home_root = home_root
        self.root.title("Book Flight")
        self.root.geometry("400x500")  # Increased height to accommodate more content
        self.root.configure(bg="#f0f0f0")  # Set background color for the window

        # Header Label
        header_label = tk.Label(
            root,
            text="Book a Flight",
            font=("Arial", 16, "bold"),
            bg="#aa4465",
            fg="white",
            padx=10,
            pady=10
        )
        header_label.pack(fill=tk.X)

        # Main Frame for Input Fields
        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(expand=True, pady=20)

        # Input Fields with Placeholder Handling
        self.name = self.create_input_field(main_frame, "Name")
        self.flight_number = self.create_input_field(main_frame, "Flight Number")
        self.departure = self.create_input_field(main_frame, "Departure")
        self.destination = self.create_input_field(main_frame, "Destination")
        self.date = self.create_input_field(main_frame, "Date (YYYY-MM-DD)")
        self.seat_number = self.create_input_field(main_frame, "Seat Number")

        # Submit Button
        submit_button = tk.Button(
            main_frame,
            text="Submit",
            command=self.save_reservation,
            font=("Arial", 12),
            bg="#ffa69e",
            fg="white",
            width=20,
            height=2,
            relief=tk.FLAT,
            activebackground="#007B9E"
        )
        submit_button.pack(pady=10)

        # Back Button
        back_button = tk.Button(
            main_frame,
            text="Back",
            command=self.go_back,
            font=("Arial", 12),
            bg="#ffa69e",
            fg="white",
            width=20,
            height=2,
            relief=tk.FLAT,
            activebackground="#c0392b"
        )
        back_button.pack(pady=10)

    def create_input_field(self, parent, placeholder):
        """Helper method to create an input field with placeholder text."""
        entry = tk.Entry(parent, width=30, font=("Arial", 12), relief=tk.FLAT)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, entry, placeholder))
        entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, entry, placeholder))
        entry.pack(pady=5)
        return entry

    def clear_placeholder(self, event, entry, placeholder):
        """Clears the placeholder text when the user focuses on the input field."""
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def restore_placeholder(self, event, entry, placeholder):
        """Restores the placeholder text if the input field is empty."""
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="gray")

    def save_reservation(self):
        """Saves the reservation details to the database after validation."""
        inputs = [
            self.name.get(),
            self.flight_number.get(),
            self.departure.get(),
            self.destination.get(),
            self.date.get(),
            self.seat_number.get()
        ]

        # Validate inputs (ensure no placeholders or empty fields)
        for i, placeholder in enumerate(["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]):
            if inputs[i] == placeholder or inputs[i] == "":
                messagebox.showerror("Error", f"Please fill out the '{placeholder}' field.")
                return

        try:
            # Save data to SQLite database
            conn = sqlite3.connect('flights.db')
            c = conn.cursor()
            c.execute("""
                INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
                VALUES (?, ?, ?, ?, ?, ?)
            """, inputs)
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Reservation saved successfully!")
            self.go_back()
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    def go_back(self):
        """Returns to the Home Page."""
        self.root.destroy()
        self.home_root.deiconify()