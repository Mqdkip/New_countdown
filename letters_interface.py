from datetime import datetime

from tkinter import *  # import everything from tkinter module
from tkinter import messagebox
import customtkinter as ctk
import functools  # import functools for button commands
import random
from random import randint  # import random and randint for sampling and number choice.

if __name__ == "__main__":
    gui = ctk.CTk()  # create a GUI window
    gui.configure(background="white")  # set the background colour of GUI window
    gui.title("Countdown")  # set the title of GUI window
    # gui.geometry("700x500")  # set the configuration of GUI window
    expression = StringVar()  # StringVar() is the variable class we create an instance of this class
    expression_field = Entry(gui, textvariable=expression)  # create the text entry box for showing the expression.
    expression_field.grid(columnspan=4,
                          ipadx=100)  # grid method is used for placing the widgets at respective positions in table like structure.

