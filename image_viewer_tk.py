from tkinter import *
from PIL import Image, ImageTk

scrn = Tk()

img1 = ImageTk.PhotoImage(Image.open("images/download.png"))
img2 = ImageTk.PhotoImage(Image.open("images/download_1.png"))
img3 = ImageTk.PhotoImage(Image.open("images/images.jfif"))
img4 = ImageTk.PhotoImage(Image.open("images/download.jfif"))
img5 = ImageTk.PhotoImage(Image.open("images/d1.jfif"))
img = [img3, img2, img1, img5, img4]

scrn.title("Photos")
scrn.iconbitmap('images/download_1.ico')

lab = Label(image=img[0])
#if you keep grid in same line grid_forget() function won't work
lab.grid(row=0, column=0, columnspan=3)

#status bar
status = Label(text="Image 1 of "+str(len(img)), bd=1, relief="sunken", anchor=E)
#anchor==textalign


def nxt(img_no):
    global lab
    global nxt_btn
    global prvs_btn
    global status

    status = Label(text="Image "+str(img_no)+" of "+str(len(img)), bd=1, relief="sunken", anchor=E)
    status.grid(row=2, columnspan=3, column=0, sticky=W+E)

    lab.grid_forget()
    lab = Label(image=img[img_no-1])
    lab.grid(row=0, column=0, columnspan=3)

    nxt_btn = Button(text="Next", command=lambda: nxt(img_no+1))
    prvs_btn = Button(text="Previous", command=lambda: back(img_no-1)).grid(row=1, column=0)

    if img_no == len(img):
        Button(text="Next", state=DISABLED).grid(row=1, column=2)
    else:
        nxt_btn.grid(row=1, column=2)


def back(img_no):
    global lab
    global nxt_btn
    global prvs_btn
    global status

    status = Label(text="Image " + str(img_no) + " of " + str(len(img)), bd=1, relief="sunken", anchor=E)
    status.grid(row=2, columnspan=3, column=0, sticky=W + E)

    lab.grid_forget()
    lab = Label(image=img[img_no-1])
    lab.grid(row=0, column=0, columnspan=3)

    nxt_btn = Button(text="Next", command=lambda: nxt(img_no+1)).grid(row=1, column=2)
    prvs_btn = Button(text="Previous", command=lambda: back(img_no-1))

    if img_no == 1:
        Button(text="Previous", state=DISABLED).grid(row=1, column=0)
    else:
        prvs_btn.grid(row=1, column=0)


nxt_btn = Button(text="Next", command=lambda: nxt(2)).grid(row=1, column=2)
prvs_btn = Button(text="Previous", state=DISABLED).grid(row=1, column=0)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
#sticky just like in compass stretching in east west

exit_button = Button(text="Exit", command=exit).grid(row=1, column=1, pady=10)

scrn.mainloop()
