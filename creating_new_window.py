from tkinter import *
from tkinter import messagebox

root = Tk()
root.iconbitmap("images/download.ico")
root.title("main window")


def scnd_click():
    global a
    messagebox.showwarning("Multiple window error", """close the window which is already running
     and run the program again""")
    a.pack_forget()
    a = Button(root, text="new window", command=btn_click)
    a.pack()


def btn_click():
    global a
    root2 = Toplevel()
    root2.iconbitmap("images/download_1.ico")
    root2.title("hello")  #if this line is not present root2 will have the same title as root

    a.destroy()
    a = Button(root, text="new window", command=scnd_click)
    a.pack()


a = Button(root, text="new window", command=btn_click)
a.pack()
root.mainloop()
