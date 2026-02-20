import tkinter as tk
from tkinter import messagebox

# Main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

tasks = []

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        update_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        tasks.clear()
        update_list()

# Function to update the listbox
def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Widgets
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(pady=5)

listbox = tk.Listbox(root, height=10, width=25)
listbox.pack(pady=10)

btn_delete = tk.Button(root, text="Delete Selected", command=delete_task)
btn_delete.pack(pady=5)

btn_clear = tk.Button(root, text="Clear All", command=clear_tasks)
btn_clear.pack(pady=5)

# Run the GUI event loop
root.mainloop()
