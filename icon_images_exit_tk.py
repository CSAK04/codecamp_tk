from tkinter import *
from PIL import ImageTk, Image

tk = Tk()

tk.title("GOOGLE")
tk.iconbitmap('images/download.ico')

img = ImageTk.PhotoImage(Image.open("images/download.png"))

lab = Label(image=img).pack()

exit_btn = Button(tk, text="exit btn", command=tk.quit).pack()

tk.mainloop()
