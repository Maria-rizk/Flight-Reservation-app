import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from edit_reservation import EditReservationPage

class ReservationsPage:
    def __init__(self, root, home_root):
        self.root = root
        self.home_root = home_root
        self.root.title("View Reservations")
        self.root.geometry("800x500")  # Increased size for better readability
        self.root.configure(bg="#f0f0f0")  # Set background color for the window

        # Header Label
        header_label = tk.Label(
            root,
            text="Flight Reservations",
            font=("Arial", 16, "bold"),
            bg="#aa4465",
            fg="white",
            padx=10,
            pady=10
        )
        header_label.pack(fill=tk.X)

        # Treeview Frame
        tree_frame = tk.Frame(root, bg="#ddfff7")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Treeview Widget
        self.tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"),
            show="headings",
            height=15
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Flight Number", text="Flight Number")
        self.tree.heading("Departure", text="Departure")
        self.tree.heading("Destination", text="Destination")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Seat Number", text="Seat Number")

        # Adjust column widths for better readability
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Name", width=150, anchor="w")
        self.tree.column("Flight Number", width=100, anchor="center")
        self.tree.column("Departure", width=100, anchor="w")
        self.tree.column("Destination", width=100, anchor="w")
        self.tree.column("Date", width=100, anchor="center")
        self.tree.column("Seat Number", width=100, anchor="center")

        # Style the Treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#ffffff",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#ffffff")
        style.map("Treeview", background=[("selected", "#4CAF50")])

        self.tree.pack(fill="both", expand=True)

        # Load reservations into the Treeview
        self.load_reservations()

        # Button Frame
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(fill="x", padx=20, pady=10)

        # Buttons with Improved Styling
        edit_button = tk.Button(
            button_frame,
            text="Edit",
            command=self.edit_reservation,
            font=("Arial", 12),
            bg="#ffa69e",
            fg="white",
            width=15,
            relief=tk.FLAT,
            activebackground="#007B9E"
        )
        edit_button.pack(side="left", padx=10)

        delete_button = tk.Button(
            button_frame,
            text="Delete",
            command=self.delete_reservation,
            font=("Arial", 12),
            bg="#ffa69e",
            fg="white",
            width=15,
            relief=tk.FLAT,
            activebackground="#c0392b"
        )
        delete_button.pack(side="left", padx=10)

        back_button = tk.Button(
            button_frame,
            text="Back",
            command=self.go_back,
            font=("Arial", 12),
            bg="#ffa69e",
            fg="white",
            width=15,
            relief=tk.FLAT,
            activebackground="#2c3e50"
        )
        back_button.pack(side="right", padx=10)

    def load_reservations(self):
        """Load reservations from the database into the Treeview."""
        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute("SELECT * FROM reservations")
        rows = c.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)
        conn.close()

    def edit_reservation(self):
        """Open the Edit Reservation Page for the selected reservation."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation to edit.")
            return
        reservation_id = self.tree.item(selected[0], "values")[0]
        self.root.withdraw()
        edit_window = tk.Toplevel()
        EditReservationPage(edit_window, self.root, reservation_id)

    def delete_reservation(self):
        """Delete the selected reservation from the database."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation to delete.")
            return
        reservation_id = self.tree.item(selected[0], "values")[0]
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this reservation?")
        if confirm:
            try:
                conn = sqlite3.connect('flights.db')
                c = conn.cursor()
                c.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
                conn.commit()
                conn.close()
                self.tree.delete(selected)
                messagebox.showinfo("Success", "Reservation deleted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def go_back(self):
        """Return to the Home Page."""
        self.root.destroy()
        self.home_root.deiconify()