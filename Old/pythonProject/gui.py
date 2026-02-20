import tkinter as tk

def greet():
    name = entry.get()
    label_output.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("Simple GUI Example")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet Me", command=greet)
button.pack()

label_output = tk.Label(root, text="")
label_output.pack()

root.mainloop()
