from tkinter import *

root = Tk()
root.title("SLIDER")
root.geometry("800x400")


def display():
    global lab
    lab = Label(root, text=vertcl.get()).pack()
    root.geometry(str(vertcl.get())+"x"+str(horzntl.get()))


vertcl = Scale(root, from_=0, to=500, length="250")
vertcl.pack()

horzntl = Scale(root, from_=800, to=0, orient=HORIZONTAL, fg="blue"
                , bg="green", length=800)
horzntl.pack()

lab = Label(root, text=vertcl.get()).pack()
btn = Button(root, text="display", command=display).pack()

root.mainloop()
