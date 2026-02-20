import tkinter as tk
from tkinter import messagebox
import os

# -------- App Setup --------
root = tk.Tk()
root.title("To-Do List")
root.geometry("350x500")

# File to store tasks
TASK_FILE = "tasks.txt"

# Theme variables
is_dark_mode = False
bg_light = "#ffffff"
fg_light = "#000000"
bg_dark = "#2e2e2e"
fg_dark = "#ffffff"

# Store task checkbuttons and variables
task_vars = []

# -------- Functions --------

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            lines = file.readlines()
            for line in lines:
                task, done = line.strip().split("|")
                var = tk.BooleanVar(value=(done == "True"))
                add_task(task, var, save=False)

def save_tasks():
    with open(TASK_FILE, "w") as file:
        for text, var in task_vars:
            file.write(f"{text}|{var.get()}\n")

def add_task(task_text=None, var=None, save=True):
    if not task_text:
        task_text = entry.get().strip()
    if not task_text:
        messagebox.showwarning("Input Error", "Please enter a task.")
        return

    if not var:
        var = tk.BooleanVar()

    cb = tk.Checkbutton(task_frame, text=task_text, variable=var,
                        bg=root["bg"], fg=fg_dark if is_dark_mode else fg_light,
                        selectcolor=root["bg"], anchor='w')
    cb.pack(fill='x', pady=2, padx=10, anchor='w')

    task_vars.append((task_text, var))
    entry.delete(0, tk.END)

    if save:
        save_tasks()

def delete_selected():
    new_task_vars = []
    for widget, (text, var) in zip(task_frame.winfo_children(), task_vars):
        if var.get():
            widget.destroy()
        else:
            new_task_vars.append((text, var))
    task_vars.clear()
    task_vars.extend(new_task_vars)
    save_tasks()

def clear_tasks():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        for widget in task_frame.winfo_children():
            widget.destroy()
        task_vars.clear()
        save_tasks()

def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode

    bg = bg_dark if is_dark_mode else bg_light
    fg = fg_dark if is_dark_mode else fg_light

    root.configure(bg=bg)
    entry.configure(bg=bg, fg=fg, insertbackground=fg)
    task_frame.configure(bg=bg)

    for widget in task_frame.winfo_children():
        widget.configure(bg=bg, fg=fg, selectcolor=bg)

# -------- Widgets --------

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Checked", command=delete_selected)
btn_delete.pack(pady=5)

btn_clear = tk.Button(root, text="Clear All", command=clear_tasks)
btn_clear.pack(pady=5)

btn_theme = tk.Button(root, text="Toggle Dark Mode", command=toggle_theme)
btn_theme.pack(pady=5)

task_frame = tk.Frame(root)
task_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Set light theme by default
toggle_theme()  # this will make it dark, so we call it again to revert
toggle_theme()

# -------- Initialize --------
load_tasks()

# -------- Run App --------
root.mainloop()
