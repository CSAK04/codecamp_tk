from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()


def open_img():
    global img
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/User/PycharmProjects"
                                               , title="Select a file to open"
                                               , filetypes=(("all files", "*.*"), ("png files", "*.png"),
                                                            ("jpg files", "*.jpg"), ("jpeg files", "*.jpeg"),
                                                            ("ico files", "*.ico"), ("jfif files", "*.jfif")))

    img = ImageTk.PhotoImage(Image.open(root.filename))

    lab = Label(image=img).pack()


Button(text="Open an image", command=open_img).pack()


root.mainloop()
