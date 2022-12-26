from tkinter import *

a=Tk()

def submit():
    w2=Label(a,text="HI "+i.get()).pack()

w=Label(a,text="ENTER YOUR NAME:").pack()
i = Entry(a)
i.pack()
b=Button(a,text="submit",command=submit).pack()


a.mainloop()
