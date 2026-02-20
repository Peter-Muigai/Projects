import tkinter as tk
from tkinter import messagebox
import math_tools
import os

def perform_operation(op):
    try:
        a = float(entry1.get())
        b = float(entry2.get()) if entry2.get() else None

        if op == 'add':
            result = math_tools.add(a, b)
            log = f"{a} + {b} = {result}"
        elif op == 'subtract':
            result = math_tools.subtract(a, b)
            log = f"{a} - {b} = {result}"
        elif op == 'multiply':
            result = math_tools.multiply(a, b)
            log = f"{a} * {b} = {result}"
        elif op == 'divide':
            result = math_tools.divide(a, b)
            log = f"{a} / {b} = {result}"
        elif op == 'power':
            result = math_tools.power(a, b)
            log = f"{a} ^ {b} = {result}"
        elif op == 'sqrt':
            result = math_tools.square_root(a)
            log = f"√{a} = {result}"

        result_label.config(text=f"Result: {result}")
        with open("history.txt", "a") as file:
            file.write(log + "\n")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def show_history():
    if os.path.exists("history.txt"):
        with open("history.txt", "r") as file:
            content = file.read()
            if not content.strip():
                messagebox.showinfo("History", "History is empty.")
            else:
                messagebox.showinfo("History", content)
    else:
        messagebox.showinfo("History", "No history found.")

def exit_app():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Smart Math Helper")

tk.Label(root, text="Enter First Number:").grid(row=0, column=0, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter Second Number (if needed):").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Add", command=lambda: perform_operation('add')).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=lambda: perform_operation('subtract')).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=lambda: perform_operation('multiply')).grid(row=3, column=0)
tk.Button(root, text="Divide", command=lambda: perform_operation('divide')).grid(row=3, column=1)
tk.Button(root, text="Power", command=lambda: perform_operation('power')).grid(row=4, column=0)
tk.Button(root, text="Square Root", command=lambda: perform_operation('sqrt')).grid(row=4, column=1)
tk.Button(root, text="View History", command=show_history).grid(row=5, column=0)
tk.Button(root, text="Exit", command=exit_app).grid(row=5, column=1)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
