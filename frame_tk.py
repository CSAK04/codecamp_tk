from tkinter import *

scrn = Tk()

frame = LabelFrame(scrn, text="hello world", pady=35, padx=34)  #inside frame padding
frame.pack(padx=160, pady=34)  #outside frame padding

b = Button(frame, text="hi").grid(row=1, column=3)

#you can use both pack and grid in the same program
#if needed use grid inside the frame

frame2 = LabelFrame(scrn, pady=40, padx=25)
frame2.pack(padx=23,pady=56)

b2 = Button(frame2,pady=3,padx=3).grid()
exit_button = Button(text="Exit", command=exit).pack(pady=10)

scrn.mainloop()
