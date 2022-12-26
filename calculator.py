# calculator
from tkinter import *


def bclick(num):
    current = inp.get()
    inp.delete(0, END)
    inp.insert(0, str(current) + str(num))


# noinspection PyGlobalUndefined
def add(a):
    num1 = inp.get()
    inp.delete(0, END)
    global sign
    sign = a
    global fnum
    fnum = float(num1)


def minus():
    add("-")


# noinspection SpellCheckingInspection
def mult():
    add("*")


def div():
    add("/")


def eq():
    num2 = float(inp.get())
    inp.delete(0, END)
    if sign == "+":
        inp.insert(1, str(fnum + num2))
    elif sign == "-":
        inp.insert(1, str(fnum - num2))
    elif sign == "*":
        inp.insert(1, str(fnum * num2))
    elif sign == "/":
        try:
            inp.insert(1, str(fnum / num2))
        except ZeroDivisionError:
            inp.insert(1, "cannot devide a number by zero")


def clear():
    inp.delete(0, END)


ca = Tk()
ca.title("calculator")

inp = Entry(ca, borderwidth=5, width=60)
inp.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

# create
b9 = Button(ca, padx=40, pady=20, text="9", command=lambda: bclick(9))
b8 = Button(ca, padx=40, pady=20, text="8", command=lambda: bclick(8))
b7 = Button(ca, padx=40, pady=20, text="7", command=lambda: bclick(7))
b6 = Button(ca, padx=40, pady=20, text="6", command=lambda: bclick(6))
b5 = Button(ca, padx=40, pady=20, text="5", command=lambda: bclick(5))
b4 = Button(ca, padx=40, pady=20, text="4", command=lambda: bclick(4))
b3 = Button(ca, padx=40, pady=20, text="3", command=lambda: bclick(3))
b2 = Button(ca, padx=40, pady=20, text="2", command=lambda: bclick(2))
b1 = Button(ca, padx=40, pady=20, text="1", command=lambda: bclick(1))
b0 = Button(ca, padx=40, pady=20, text="0", command=lambda: bclick(0))

bplus = Button(ca, padx=40, pady=20, text="+", command=lambda: add("+"))
bmins = Button(ca, padx=40, pady=20, text="-", command=minus)
binto = Button(ca, padx=40, pady=20, text="*", command=mult)
bdiv = Button(ca, padx=40, pady=20, text="/", command=div)

bequal = Button(ca, padx=40, pady=20, text="=", command=eq)
bclear = Button(ca, padx=40, pady=20, text="C", command=clear)

# packing
b9.grid(column=2, row=1)
b8.grid(column=1, row=1)
b7.grid(column=0, row=1)
b6.grid(column=2, row=2)
b5.grid(column=1, row=2)
b4.grid(column=0, row=2)
b3.grid(column=2, row=3)
b2.grid(column=1, row=3)
b1.grid(column=0, row=3)
b0.grid(column=0, row=4)

bclear.grid(column=3, row=1)
bequal.grid(column=3, row=4, columnspan=1)

bplus.grid(column=3, row=2)
bmins.grid(column=3, row=3)
binto.grid(column=1, row=4)
bdiv.grid(column=2, row=4)

ca.mainloop()
