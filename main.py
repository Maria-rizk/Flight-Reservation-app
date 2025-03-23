import tkinter as tk
from home import HomePage
from database import create_database  # Import the function

if __name__ == "__main__":
    create_database()  # Create the table before launching the app
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()