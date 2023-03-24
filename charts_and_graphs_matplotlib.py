from tkinter import *
import numpy as np
import matplotlib.pyplot as pp

root = Tk()
root.title("charts and graphs")
root.iconbitmap("images/download_1.ico")
root.geometry("700x400")


def graph():
    house_price = np.random.normal(200000, 20000, 5)
    pp.polar(house_price)
    pp.show()


def graph2():
    house_price = np.random.normal(200000, 20000, 5000)
    pp.hist(house_price, 100)
    pp.show()


graph_btn = Button(root, text="display polar graph", command=graph, font=("Ariel", 45))
graph_btn.pack(ipady=20, ipadx=100)

graph_btn = Button(root, text="display hist graph", command=graph2, font=("Ariel", 45))
graph_btn.pack(ipady=20, ipadx=100)
root.mainloop()
