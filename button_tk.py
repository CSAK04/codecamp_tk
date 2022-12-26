from tkinter import *

a=Tk()

def clicked():
    label=Label(a,text="you clicked toooooo haaaard!!!!!!!!!!!!")
    label.pack()

b1=Button(a,text="click me",padx=32,pady=10,command=clicked,fg="blue",bg="green")

b1.pack()


a.mainloop()
