from tkinter import *  # import everything from tkinter module
import functools  # import functools for button commands
import random
from random import randint  # import random and randint for sampling and number choice.


# Making the big number and developing all possible solutions
def making():
    big_options = [25, 50, 75, 100]
    small_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_of_big = int(input("How many big numbers: "))
    #number_of_big = clicked.get()
    lob = random.sample(big_options, number_of_big)  # big numbers used in number list
    los = random.sample(small_options, (6 - number_of_big))  # small numbers used in number list
    global numbers
    numbers = [*los, *lob]
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
        pass
        #print(s)
    print(f"There are a total of {len(final)} solutions.")
    #button_making(numbers)



def switch():
    if buttonc["state"] == "normal":
        buttonc["state"] = "disabled"
        button0["state"] = "disabled"
        button1["state"] = "disabled"
        button2["state"] = "disabled"
        button3["state"] = "disabled"
        button4["state"] = "disabled"
        button5["state"] = "disabled"


    else:
        buttonc["state"] = "normal"
        button0["state"] = "normal"
        button1["state"] = "normal"
        button2["state"] = "normal"
        button3["state"] = "normal"
        button4["state"] = "normal"
        button5["state"] = "normal"

def number_press_delete(b, n):
    press(n)
    switch()
    b.grid_forget()


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

#def show():
 #   label.config(text=clicked.get())
  #  dropdownsend.destroy()
    # print(clicked.get())



def operand_press_switch(op):
    press(op)
    switch()



#def button_making(numbers):
if __name__ == "__main__":
    gui = Tk()  # create a GUI window
    gui.configure(background="white")  # set the background colour of GUI window
    gui.title("Countdown")  # set the title of GUI window
    #gui.geometry("700x500")  # set the configuration of GUI window
    equation = StringVar()  # StringVar() is the variable class we create an instance of this class
    expression_field = Entry(gui, textvariable=equation)  # create the text entry box for showing the expression.
    expression_field.grid(columnspan=4,ipadx=100)  # grid method is used for placing the widgets at respective positions in table like structure.
    making()




buttonc = Button(gui, text=f'Constant button')




button0 = Button(gui, text=f' {numbers[0]} ', fg='black', bg='white', padx = 16, pady = 16, bd = 8, font = ('arial', 20, 'bold'))
button0.configure(command=functools.partial(number_press_delete, button0, numbers[0]))
button0.grid(row=2, column=0)

button1 = Button(gui, text=f' {numbers[1]} ', fg='black', bg='white', padx = 16, pady = 16, bd = 8, font = ('arial', 20, 'bold'))
button1.configure(command=functools.partial(number_press_delete, button1, numbers[1]))
button1.grid(row=2, column=1)

button2 = Button(gui, text=f' {numbers[2]} ', fg='black', bg='red', padx = 16, pady = 16, bd = 8, font = ('arial', 20, 'bold'))
button2.configure(command=functools.partial(number_press_delete, button2, numbers[2]))
button2.grid(row=2, column=2)

button3 = Button(gui, text=f' {numbers[3]} ', fg='black', bg='red', padx = 16, pady = 16, bd = 8, font = ('arial', 20, 'bold'))
button3.configure(command=functools.partial(number_press_delete, button3, numbers[3]))
button3.grid(row=3, column=0)

button4 = Button(gui, text=f' {numbers[4]} ', fg='black', bg='red', padx = 16, pady = 16, bd = 8, font = ('arial', 20, 'bold'))
button4.configure(command=functools.partial(number_press_delete, button4, numbers[4]))
button4.grid(row=3, column=1)

button5 = Button(gui, text=f' {numbers[5]} ', fg='black', bg='red', padx = 16, pady = 16, bd = 8, font = ('arial', 20, 'bold'))
button5.configure(command=functools.partial(number_press_delete, button5, numbers[5]))
button5.grid(row=3, column=2)


# Create button, it will change label text
#dropdownsend = Button(gui, text="Click to Confirm", command=show)
#dropdownsend.grid(row=3, column=4)

# Create Label
label = Label(gui, text=" ")

# operation buttons
plus = Button(gui, text=' + ', fg='black', bg='red', height=1, width=7)
plus.configure(command=functools.partial(operand_press_switch, ' + '))
plus.grid(row=2, column=3)

minus = Button(gui, text=' - ', fg='black', bg='red', height=1, width=7)
minus.configure(command = functools.partial(operand_press_switch, '-'))
minus.grid(row=3, column=3)

multiply = Button(gui, text=' * ', fg='black', bg='red', height=1, width=7)
multiply.configure(command = functools.partial(operand_press_switch, '*'))
multiply.grid(row=4, column=3)

divide = Button(gui, text=' / ', fg='black', bg='red', height=1, width=7)
divide.configure(command = functools.partial(operand_press_switch, '/'))
divide.grid(row=5, column=3)

equal = Button(gui, text=' = ', fg='black', bg='red',
               command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

clear = Button(gui, text='Clear', fg='black', bg='red',
               command=clear, height=1, width=7)
clear.grid(row=5, column='1')

Lbracket = Button(gui, text='(', fg='black', bg='red',
                  command=lambda: press('('), height=1, width=7)
Lbracket.grid(row=6, column=1)

Rbracket = Button(gui, text=')', fg='black', bg='red',
                  command=lambda: press(')'), height=1, width=7)
Rbracket.grid(row=6, column=2)

reset = Button(gui, text='Reset', fg='black', bg='red',
               command=making, height=1, width=7)
reset.grid(row=7, column=1)


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