import tkinter as tk
import defictions

laki = tk.Tk()
laki.geometry("350x460")
laki.title("started")

text = tk.Text(laki, width = 25, height = 1, font = ("arial", 15))
text.pack(pady = 10)

text.insert(1.0, "   insert your sentence here :")

entry = tk.Entry(laki, width = 20, font = ("arial", 15))
entry.pack(pady = 15)

n = 0

output_text = tk.Text(laki, width = 15, height = 1, font = ("arial", 14))
output_text.pack(pady = 20)

def btn():
    
    global n
        
    output_text.delete(1.0, "end")
    input_sentence = entry.get()
    output_text.insert(1.0, defictions.starting(input_sentence))
    

button = tk.Button(laki, font = ("arial", 17), height = 3, width = 17, text = "tap to save sentence", command = btn)
button.pack(pady = 10)






laki.mainloop()