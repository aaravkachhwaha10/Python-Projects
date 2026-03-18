import tkinter as tk
from tkinter import messagebox

def calculate_bill():
    try:
        units = float(unit_entry.get())

        if units < 0:
            messagebox.showerror("Error", "Units cannot be negative!")
            return
        if units<= 100:
            bill = units * 0.12
        elif units <= 300:
            bill = 100 * 0.12 + (units - 100) * 0.15
        else:
            bill = 100 * 0.12 + 200 * 0.15 + (units - 300) * 0.20
        
        result_label.config(text=f "Energy Bill: $(bill:.2f)")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of units!")