import tkinter as tk
import defictions_prsn
import defictions_En
import defictions_mixed
import lang_finder
import lang_many_finder

laki = tk.Tk()
laki.geometry("750x460")
laki.title("sentence type detect")
laki.config(bg="#1e1e1e")

lbl1 = tk.Label(
    laki,
    text="Insert your sentence:",
    font=("Arial", 16, "bold"),
    fg="purple",
    bg="#1e1e1e"
)

lbl1.place(x=40, y=15)

ntr1 = tk.Entry(
    laki,
    font = ("arial", 20),
    width=17,
    justify="center"
)
ntr1.place(x=26, y=60)


output_text1 = tk.Text(
    laki,
    width=18,
    height=1,
    font=("Arial", 14),
    bg="#2d2d2d",
    fg="#00ffcc",
    relief="flat"
)
output_text1.place(x=40, y=150)

lbl2 = tk.Label(
    laki,
    font=("arial", 16),
    text="language :",
    fg="orange",
    bg="#1e1e1e",
    justify="center",
    relief="flat"
)
lbl2.place(x=88, y=335)

output_text2 = tk.Text(
    laki,
    width=18,
    height=1,
    font=("arial", 14),
    bg="#2d2d2d",
    fg="#00ffcc",
    relief="flat"
)
output_text2.place(x=40, y=400)

lbl3 = tk.Label(
    laki,
    font=("arial", 16, "bold"),
    text = "language percents :",
    fg = "red",
    bg = "#1e1e1e",
    justify = "center",
    relief  = "flat"
)
lbl3.place(x=400, y=12)


txt1 = tk.Text(
    laki,
    font = ("arial", 16),
    width = 16,
    height = 1,
    fg = "white",
    bg = "#2d2d2d",
    relief = "flat"
)

txt1.place(x=320, y=70)


txt2 = tk.Text(
    laki,
    font = ("arial", 16),
    width = 16,
    height = 1,
    fg = "white",
    bg = "#2d2d2d",
    relief = "flat"
)

txt2.place(x=540, y=70)

txt3 = tk.Text(
    laki,
    font = ("arial", 16),
    width = 16,
    height = 1,
    fg = "white",
    bg = "#2d2d2d",
    relief = "flat"
)

txt3.place(x=320, y=120)

lbl4 = tk.Label(
    laki,
    font = ("arial", 16, "bold"),
    text = "sentence components :",
    fg = "lightgreen",
    bg = "#1e1e1e",
    relief = "flat",
    justify = "center"
)

lbl4.place(x=400, y=200)

txt4 = tk.Text(
    laki,
    font = ("arial", 16),
    width = 16,
    height = 1,
    fg = "white",
    bg = "#2d2d2d",
    relief = "flat"
)

txt4.place(x=320, y=270)

txt5 = tk.Text(
    laki,
    font = ("arial", 16),
    width = 16,
    height = 1,
    fg = "white",
    bg = "#2d2d2d",
    relief = "flat"
)

txt5.place(x=540, y=270)

txt6 = tk.Text(
    laki,
    font = ("arial", 16),
    width = 16,
    height = 1,
    fg = "white",
    bg = "#2d2d2d",
    relief = "flat"
)

txt6.place(x=320, y=320)


def btn():
    output_text1.delete(1.0, "end")
    output_text2.delete(1.0, "end")
    txt1.delete(1.0, "end")
    txt2.delete(1.0, "end")
    txt3.delete(1.0, "end")
    txt4.delete(1.0, "end")
    txt5.delete(1.0, "end")
    txt6.delete(1.0, "end")
    input_sentence = ntr1.get()
    list_of_langs =  lang_finder.language_percent_find(input_sentence)
    list_of_langcount = lang_many_finder.lang_finding(input_sentence)
    
    txt1.insert(1.0, f"en : {list_of_langs[1]}")
    txt2.insert(1.0, f"prsn : {list_of_langs[0]}")
    txt3.insert(1.0, f"other : {list_of_langs[2]}")
    txt4.insert(1.0, f"en : {list_of_langcount[1]}")
    txt5.insert(1.0, f"prsn : {list_of_langcount[0]}")
    txt6.insert(1.0, f"other : {list_of_langcount[2]}")
    
    if list_of_langs[0] == 100.0:

        output_text1.insert(1.0, defictions_prsn.starting(input_sentence))
        output_text2.insert(1.0, "persian")

    elif list_of_langs[1] == 100.0:

        output_text1.insert(1.0, defictions_En.starting(input_sentence))
        output_text2.insert(1.0, "english")

    elif list_of_langs[2] == 100.0:

        output_text1.insert(1.0, "unsupported language")
        output_text2.insert(1.0, "other language")

    else:

        if list_of_langs[2] == 0.0:

            output_text1.insert(1.0, defictions_mixed.starting(input_sentence))
            output_text2.insert(1.0, "mixed language")

        elif list_of_langs[2] != 0.0:

            output_text1.insert(1.0, "unsupported language")
            output_text2.insert(1.0, "other language")
        
        else:

            output_text1.insert(1.0, "unsupported text")
            output_text2.insert(1.0, "unsupport text")


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

button.place(x=40, y=235)



laki.mainloop()
