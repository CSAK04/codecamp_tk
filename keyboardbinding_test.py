import tkinter.messagebox
from tkinter import *

a = Tk()


def event(b):
    print(b)
    if b.char == "\r":
        print("enter")


a.bind("<Key>", event)

a.mainloop()
