#todo Undo button

import tkinter
from datetime import datetime
from tkinter import *  # import everything from tkinter module
from tkinter import messagebox

import customtkinter as ctk
import functools  # import functools for button commands
import random
from random import randint  # import random and randint for sampling and number choice.
import time
import datetime


# ctk.set_default_color_theme("dark-red")
# Making the big number and developing all possible solutions
def making():
    big_options = [25, 50, 75, 100]
    small_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_of_big = int(input("How many big numbers: "))
    # number_of_big = clicked.get()
    lob = random.sample(big_options, number_of_big)  # big numbers used in number list
    los = random.sample(small_options, (6 - number_of_big))  # small numbers used in number list
    global numbers
    numbers = [*los, *lob]
    global target
    target = randint(100, 999)
    print(f"The aim is to make {target} using {numbers}")
    solutions = list()
    solve(target, numbers, list(), solutions)
    unique = list()
    final = list()
    for s in solutions:
        a = ''.join(sorted(s))
        if not a in unique:
            unique.append(a)
            final.append(s)
    for s in final:  # print them out
        #pass
        print(s)
    print(f"There are a total of {len(final)} solutions.")
    # button_making(numbers)


def switch():
    if buttonc["state"] == "normal":
        buttonc.configure(state="disabled")
        button0.configure(state="disabled")
        button1.configure(state="disabled")
        button2.configure(state="disabled")
        button3.configure(state="disabled")
        button4.configure(state="disabled")
        button5.configure(state="disabled")
        plus.configure(state="normal")
        minus.configure(state="normal")
        multiply.configure(state="normal")
        divide.configure(state="normal")

    else:
        buttonc.configure(state="normal")
        button0.configure(state="normal")
        button1.configure(state="normal")
        button2.configure(state="normal")
        button3.configure(state="normal")
        button4.configure(state="normal")
        button5.configure(state="normal")
        plus.configure(state = "disabled")
        minus.configure(state = "disabled")
        multiply.configure(state = "disabled")
        divide.configure(state = "disabled")


def number_press_delete(b, n):
    press(n)
    switch()
    b.grid_remove()


def solve(target, numbers, path, solutions):
    if len(numbers) == 1:
        return
    distinct = sorted(list(set(numbers)), reverse=True)
    remainder = list(distinct)
    for n1 in distinct:  # reduce list by combining a pair
        remainder.remove(n1)
        for n2 in remainder:
            rem2 = list(
                numbers)  # in case of duplicates we need to start with full list and take out the n1,n2 pair of elements
            rem2.remove(n1)
            rem2.remove(n2)
            combine(target, solutions, path, rem2, n1, n2, '+')
            combine(target, solutions, path, rem2, n1, n2, '-')
            if n2 > 1:
                combine(target, solutions, path, rem2, n1, n2, '*')
                if not n1 % n2:
                    combine(target, solutions, path, rem2, n1, n2, '//')


def combine(target, solutions, path, rem2, n1, n2, symb):
    lst = list(rem2)
    ans = eval("{0}{2}{1}".format(n1, n2, symb))
    newpath = path + ["{0}{3}{1}={2}".format(n1, n2, ans, symb[0])]
    if ans == target:
        solutions += [newpath]
    else:
        lst.append(ans)
        solve(target, lst, newpath, solutions)


# Button initialisation

# On click of a button, the result enters the expression bar
expression = ""


def press(num):
    global expression
    expression = expression + str(num)  # Concatenation of string
    equation.set(expression)  # Update the expression by using set method


# Function to evaluate the final expression
def equalpress():
    try:  # Try and except statement is used for handling the errors like zero
        global expression
        total = str(eval(expression))
        equation.set(total)
        print(total)
        expression = ""  # initialize the expression variable
    # if error is generate then handle by the except block
    except:
        equation.set(" error ")
        expression = ""


# Function to clear the contents of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# create a Buttons and place at a particular location inside the root window .
# when user press the button, the command or function affiliated to that button is executed .

# def show():
#   label.config(text=clicked.get())
#  dropdownsend.destroy()
# print(clicked.get())


def operand_press_switch(op):
    press(op)
    switch()

def remember():
    if not button1.winfo_viewable():
        button1.grid()


# def button_making(numbers):
if __name__ == "__main__":
    gui = ctk.CTk()  # create a GUI window
    gui.configure(background="white")  # set the background colour of GUI window
    gui.title("Countdown")  # set the title of GUI window
    # gui.geometry("700x500")  # set the configuration of GUI window
    equation = StringVar()  # StringVar() is the variable class we create an instance of this class
    expression_field = Entry(gui, textvariable=equation)  # create the text entry box for showing the expression.
    expression_field.grid(columnspan=4,
                          ipadx=100)  # grid method is used for placing the widgets at respective positions in table like structure.
    making()

brn = 0 #base row number




target_label = ctk.CTkButton(gui, text = f"Target is {target}",text_color=("red"))
target_label.configure(state = "disabled", fg_color='red', text_color_disabled='white')
target_label.grid(row = brn+1, column = 0)

buttonc = Button(gui, text=f'Constant button')

button0 = ctk.CTkButton(gui, text=f' {numbers[0]} ', font=('arial', 20, 'bold'))
button0.configure(command=functools.partial(number_press_delete, button0, numbers[0]))
button0.grid(row=brn+3, column=0)

button1 = ctk.CTkButton(gui, text=f' {numbers[1]} ', font=('arial', 20, 'bold'))
button1.configure(command=functools.partial(number_press_delete, button1, numbers[1]))
button1.grid(row=brn+3, column=1)

button2 = ctk.CTkButton(gui, text=f' {numbers[2]} ', font=('arial', 20, 'bold'))
button2.configure(command=functools.partial(number_press_delete, button2, numbers[2]))
button2.grid(row=brn+3, column=2)

button3 = ctk.CTkButton(gui, text=f' {numbers[3]} ', font=('arial', 20, 'bold'))
button3.configure(command=functools.partial(number_press_delete, button3, numbers[3]))
button3.grid(row=brn+4, column=0)

button4 = ctk.CTkButton(gui, text=f' {numbers[4]} ', font=('arial', 20, 'bold'))
button4.configure(command=functools.partial(number_press_delete, button4, numbers[4]))
button4.grid(row=brn+4, column=1)

button5 = ctk.CTkButton(gui, text=f' {numbers[5]} ', font=('arial', 20, 'bold'))
button5.configure(command=functools.partial(number_press_delete, button5, numbers[5]))
button5.grid(row=brn+4, column=2)

# Create button, it will change label text
# dropdownsend = Button(gui, text="Click to Confirm", command=show)
# dropdownsend.grid(row=3, column=4)

# Create Label
#label = Label(gui, text=" ")

# operation buttons
plus = ctk.CTkButton(gui, text=' + ')
plus.configure(command=functools.partial(operand_press_switch, ' + '))
plus.grid(row=brn+3, column=3)

minus = ctk.CTkButton(gui, text=' - ')
minus.configure(command=functools.partial(operand_press_switch, '-'))
minus.grid(row=brn+4, column=3)

multiply = ctk.CTkButton(gui, text=' * ')
multiply.configure(command=functools.partial(operand_press_switch, '*'))
multiply.grid(row=brn+5, column=3)

divide = ctk.CTkButton(gui, text=' / ')
divide.configure(command=functools.partial(operand_press_switch, '/'))
divide.grid(row=brn+6, column=3)

equal = ctk.CTkButton(gui, text=' = ', command=equalpress)
equal.grid(row=brn+6, column=2)

clear = ctk.CTkButton(gui, text='Clear', command=clear)
clear.grid(row=brn+5, column='0')


undo_button = ctk.CTkButton(gui, text = 'Undo', font=('arial', 20, 'bold'))
undo_button.configure(command=remember())
undo_button.grid(row=brn+6, column=0)

Lbracket = ctk.CTkButton(gui, text='(', command=lambda: press('('))
Lbracket.grid(row=brn+5, column=1)

Rbracket = ctk.CTkButton(gui, text=')', command=lambda: press(')'))
Rbracket.grid(row=brn+5, column=2)

#reset = ctk.CTkButton(gui, text='Reset', command=making)
#reset.grid(row=brn+6, column=1)

timer_string_var = ctk.StringVar(gui)
time_b = ctk.CTkButton(gui, textvariable=timer_string_var)
time_b.configure(state="disabled", fg_color='red', text_color_disabled='white')
time_b.grid(row=brn + 1, column=1)

t_seconds = 30


def update_gui():
    global t_seconds
    timer = datetime.timedelta(seconds=t_seconds)
    timer_string_var.set(timer)
    t_seconds -= 1
    if (t_seconds == 0):
        messagebox.showinfo("Time Countdown", "Time's up ")
    gui.update()
    gui.after(1000, update_gui)

gui.after(1000, update_gui)






# while t_seconds > 0:
#     timer = datetime.timedelta(seconds = t_seconds)
#     time.sleep(1)
#     t_seconds -= 1
#     time_b = ctk.CTkButton(gui, text=f"Time left is {timer}")
#     time_b.configure(state="disabled", fg_color='red', text_color_disabled='white')
#     time_b.grid(row=brn + 1, column=1)
#     gui.update()





gui.mainloop()  # start the GUI

# nobtions = [
#     "1",
#     "2",
#     "3",
#     "4", ]
#
# clicked = IntVar()
# clicked.set("Number of Big Numbers")
#
# # Create Dropdown menu
# dropdown = OptionMenu(gui, clicked, *nobtions)
# dropdown.grid(row=2, column=4)
