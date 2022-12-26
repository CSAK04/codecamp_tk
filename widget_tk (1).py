from tkinter import *

main=Tk()

#create
mylabel = Label(main,text="hello_world")
mylabel1=Label(main,text="1001993")
mylabel2= Label(main,text="hell0")
mylabel3= Label(main,text="hellfjjnnnasmdm")
#grid metheod
mylabel.grid(row=0,column=0)
mylabel1.grid(row=0,column=1)
mylabel2.grid(row=1,column=1)
mylabel3.grid(row=1,column=34)#it is visible at next line because grid works relative
"""try resizing the window
without code!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""

main.mainloop()
