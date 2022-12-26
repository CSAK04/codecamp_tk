from tkinter import *

scrn = Tk()

a = IntVar()

def click(s):
    global label
    label = Label(text=s).pack()


Radiobutton(scrn, text="a", variable=a, value=1, command=lambda: click(a.get())).pack()
Radiobutton(scrn, text="b", variable=a, value=2, command=lambda: click(a.get())).pack()
Radiobutton(scrn, text="c", variable=a, value=3, command=lambda: click(a.get())).pack()

label = Label(text=a.get())
label.pack()

Button(scrn, text="click", command=lambda: click(a.get())).pack()
scrn.mainloop()
