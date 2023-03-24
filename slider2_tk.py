from tkinter import *

root = Tk()
root.title("SLIDER")
root.geometry("800x400")


def display(a):
    root.geometry(str(horzntl.get())+"x"+str(vertcl.get()))


vertcl = Scale(root, from_=100, to=500, length="250", command=display)
vertcl.pack()

horzntl = Scale(root, from_=800, to=100, orient=HORIZONTAL, fg="blue", command=display,
                bg="green", length=800)
horzntl.pack()

root.mainloop()
