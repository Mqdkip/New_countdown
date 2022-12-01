from tkinter import *
import functools

fenster = Tk()
fenster.title("Window")

def switch():
    if bc["state"] == "normal":
        bc["state"] = "disabled"
        b1["state"] = "disabled"
        b3["state"] = "disabled"
        b2["text"] = "enable"
    else:
        bc["state"] = "normal"
        b1["state"] = "normal"
        b3["state"] = "normal"
        b2["text"] = "disable"

def basic():
    print('hi')
    
def basic_switch():
    basic()
    switch()

#--Buttons
bc = Button(fenster, text = 'Constant button', height = 6, width = 9)
bc.grid(row = 1, column = 2)
b1 = Button(fenster, text="Button", height=5, width=7)

b1.grid(row=0, column=0)
b3 = Button(fenster, text="Button", height=5, width=7)
b1.configure(command = functools.partial(basic_switch))
b3.configure(command = functools.partial(basic_switch))
b3.grid(row=2, column=2)    

b2 = Button(text="disable", command=switch)
b2.grid(row=0, column=1)

fenster.mainloop()