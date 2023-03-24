from tkinter import *

root = Tk()
root.title("checkboxes")


def clicka():
    global lab1
    lab1 = Label(root, text=a.get()).pack()


def clickb():
    global lab2
    lab2 = Label(root, text=b.get()).pack()


a = IntVar()
b = StringVar()

A = Checkbutton(root, text="Option 1", variable=a, command=clicka)
A.deselect()
A.pack()
B = Checkbutton(root, text="Option 2", variable=b, command=clickb, onvalue="on", offvalue="off")
B.deselect()
B.pack()

lab1 = Label(root, text=a.get()).pack()
lab2 = Label(root, text=b.get()).pack()

root.mainloop()
