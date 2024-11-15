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
        label1 = ttk.Label(frame, text="Restaurant Management App", font=("Lucida Console", 15, "bold"))
        label1.grid(row=0, columnspan=3, padx=10, pady=10)
        self.menu_labels = {}
        self.menu_quantities = {}
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            i_labels = ttk.Label(frame, text=f"{item.upper()} (${price}):", font=("Calibri", 12))
            i_labels.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = i_labels
            q_entries = ttk.Entry(frame, width=5)
            q_entries.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = q_entries
        self.currency_var = StringVar()
        cur_lbl = ttk.Label(frame, text="Currency:", font=("Modern No. 20", 12))
        cur_lbl.grid(row=len(self.menu_items) + 1, column=0, padx=10, pady=5)
        cur_sel = ttk.Combobox(frame, textvariable=self.currency_var, state="readonly", width=18, values=("USD ($)", "INR (₹)"))
        cur_sel.grid(row=len(self.menu_items) + 1, column=1, padx=10, pady=5)
        cur_sel.current(0)
        self.currency_var.trace_add("write", self.update_menu_prices)
        place_order_btn = ttk.Button(frame, text="Place Order", command=self.place_order)
        place_order_btn.grid(row=len(self.menu_items) + 2, columnspan=3, padx=10, pady=10)
    
    def setup_bg(self, root):
        BG_WIDTH = 800
        BG_HEIGHT = 600
        canva = Canvas(root, width=BG_WIDTH, height=BG_HEIGHT)
        canva.pack()
        or_img = PhotoImage(file="bg.png")
        bg_img = or_img.subsample(
            or_img.width() // BG_WIDTH,
            or_img.height() // BG_HEIGHT)
        canva.create_image(0, 0, anchor=NW, image=bg_img)
        canva.image = bg_img

    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR (₹)" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR (₹)" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_quantities[item] * rate
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_summary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item")

if __name__ == "__main__":
    root = Tk()
    app = Rest_manag(root)
    root.mainloop()