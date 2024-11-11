from tkinter import *
from tkinter import ttk, messagebox

class Rest_manag:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.menu_items = {"Fried Rice" : 2,
                           "Schezwan Noodles" : 3,
                           "Pizza" : 4,
                           "Masala Dosa" : 3,
                           "Gobi 65" : 5,
                           "South Indian Thali" : 6}
        self.exchange_rate = 85
        self.setup_bg(self.root)
        frame = ttk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        label = ttk.Label(frame, text="Restaurant MAnagement App", font=("Lucida Console", 15, "bold"))
        label.grid(row=0, columnspan=3, padx=10, pady=10)
        self.menu_labels = {}
        self.menu_quantities = {}
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            i_labels = ttk.Label(frame, text=f"{item.upper()} (${price})", font=("Calibri", 12))
            i_labels.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = i_labels
            q_entries = ttk.Entry(frame, width=5)
            q_entries.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = q_entries
            