#Creating radio btn with loop
from tkinter import *


def click(s):
    global label
    label = Label(text=s).pack(anchor=E)


a = Tk()

main = [
    ("MANGO", "MANGO"),
    ("APPLE", "APPLE"),
    ("ORANGE", "ORANGE")
]

r = StringVar()
r.set("MANGO")

for text, value in main:
    Radiobutton(a, text=text, variable=r, value=value).pack(anchor=W)

Button(a, text="ADD", command=lambda: click(r.get())).pack()
a.mainloop()
