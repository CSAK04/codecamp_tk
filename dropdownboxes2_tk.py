from tkinter import *

root = Tk()


def btn_click():
    Label(text=clicked.get()).pack()


options = ["Sunday", "Monday", "Tuesday", "Wednesday"]

clicked = StringVar()
clicked.set(options[0])  #makes sunday default value of dropdown

a = OptionMenu(root, clicked, *options)
a.pack()

btn = Button(text="Show Selection", command=btn_click)
btn.pack()

root.mainloop()
