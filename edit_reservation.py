import tkinter as tk
from tkinter import messagebox
import sqlite3

class EditReservationPage:
    def __init__(self, root, reservations_root, reservation_id):
        self.root = root
        self.reservations_root = reservations_root
        self.reservation_id = reservation_id
        self.root.title("Edit Reservation")
        self.root.geometry("400x500")  # Increased height to accommodate more content
        self.root.configure(bg="#f0f0f0")  # Set background color for the window

        # Fetch reservation details from the database
        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute("SELECT * FROM reservations WHERE id=?", (reservation_id,))
        self.reservation = c.fetchone()
        conn.close()

        # Header Label
        header_label = tk.Label(
            root,
            text="Edit Reservation",
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
        self.name = self.create_input_field(main_frame, "Name", self.reservation[1])
        self.flight_number = self.create_input_field(main_frame, "Flight Number", self.reservation[2])
        self.departure = self.create_input_field(main_frame, "Departure", self.reservation[3])
        self.destination = self.create_input_field(main_frame, "Destination", self.reservation[4])
        self.date = self.create_input_field(main_frame, "Date (YYYY-MM-DD)", self.reservation[5])
        self.seat_number = self.create_input_field(main_frame, "Seat Number", self.reservation[6])

        # Update Button
        update_button = tk.Button(
            main_frame,
            text="Update",
            command=self.update_reservation,
            font=("Arial", 12),
            bg="#ffa69e",
            fg="white",
            width=20,
            height=2,
            relief=tk.FLAT,
            activebackground="#ddfff7"
        )
        update_button.pack(pady=10)

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
            activebackground="#ddfff7"
        )
        back_button.pack(pady=10)

    def create_input_field(self, parent, placeholder, default_value):
        """Helper method to create an input field with placeholder text."""
        entry = tk.Entry(parent, width=30, font=("Arial", 12), relief=tk.FLAT)
        entry.insert(0, default_value)
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

    def update_reservation(self):
        """Updates the reservation details in the database after validation."""
        inputs = [
            self.name.get(),
            self.flight_number.get(),
            self.departure.get(),
            self.destination.get(),
            self.date.get(),
            self.seat_number.get()
        ]

        # Validate inputs (ensure no placeholders or empty fields)
        placeholders = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
        for i, placeholder in enumerate(placeholders):
            if inputs[i] == placeholder or inputs[i] == "":
                messagebox.showerror("Error", f"Please fill out the '{placeholder}' field.")
                return

        try:
            # Update data in SQLite database
            conn = sqlite3.connect('flights.db')
            c = conn.cursor()
            c.execute("""
                UPDATE reservations
                SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
                WHERE id=?
            """, (*inputs, self.reservation_id))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Reservation updated successfully!")
            self.go_back()
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    def go_back(self):
        """Returns to the Reservations Page."""
        self.root.destroy()
        self.reservations_root.deiconify()