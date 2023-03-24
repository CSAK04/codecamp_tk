from tkinter import *

root = Tk()


def cli(q):
    global label
    label = Label(text=clicked.get()).pack()


def btn_click():
    Label(text=clicked.get()).pack()


clicked = StringVar()
clicked.set("Sunday")  #makes sunday default value of dropdown

a = OptionMenu(root, clicked, "Sunday", "Monday", "Tuesday", command=cli)
a.pack()

label = Label(root, text=clicked.get()).pack()

btn = Button(text="Show Selection", command=btn_click)
btn.pack()

root.mainloop()
