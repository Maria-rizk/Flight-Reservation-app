import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from edit_reservation import EditReservationPage

class ReservationsPage:
    def __init__(self, root, home_root):
        self.root = root
        self.home_root = home_root
        self.root.title("View Reservations")
        self.root.geometry("600x400")

        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Flight Number", text="Flight Number")
        self.tree.heading("Departure", text="Departure")
        self.tree.heading("Destination", text="Destination")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Seat Number", text="Seat Number")
        self.tree.pack(fill="both", expand=True)

        self.load_reservations()

        tk.Button(root, text="Edit", command=self.edit_reservation, width=20).pack(side="left", padx=10, pady=10)
        tk.Button(root, text="Delete", command=self.delete_reservation, width=20).pack(side="left", padx=10, pady=10)
        tk.Button(root, text="Back", command=self.go_back, width=20).pack(side="right", padx=10, pady=10)

    def load_reservations(self):
        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute("SELECT * FROM reservations")
        rows = c.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)
        conn.close()

    def edit_reservation(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation to edit.")
            return
        reservation_id = self.tree.item(selected[0], "values")[0]
        self.root.withdraw()
        edit_window = tk.Toplevel()
        EditReservationPage(edit_window, self.root, reservation_id)

    def delete_reservation(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation to delete.")
            return
        reservation_id = self.tree.item(selected[0], "values")[0]
        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation deleted!")
        self.tree.delete(selected)

    def go_back(self):
        self.root.destroy()
        self.home_root.deiconify()