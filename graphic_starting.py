import tkinter as tk
import defictions

laki = tk.Tk()
laki.geometry("350x460")
laki.title("Started")
laki.config(bg="#1e1e1e")


title = tk.Label(
    laki,
    text="Insert your sentence:",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=15)


entry = tk.Entry(
    laki,
    width=22,
    font=("Arial", 15),
    justify="center"
)
entry.pack(pady=10)


output_text = tk.Text(
    laki,
    width=18,
    height=1,
    font=("Arial", 14),
    bg="#2d2d2d",
    fg="#00ffcc",
    relief="flat"
)
output_text.pack(pady=25)

def btn():
    output_text.delete(1.0, "end")
    input_sentence = entry.get()
    output_text.insert(1.0, defictions.starting(input_sentence))


button = tk.Button(
    laki,
    text="Save",
    font=("Arial", 15, "bold"),
    bg="#00adb5",
    fg="white",
    activebackground="#008b8b",
    relief="flat",
    height=2,
    width=15,
    command=btn
)
button.pack(pady=20)

laki.mainloop()
