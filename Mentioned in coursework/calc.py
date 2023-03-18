# import everything from tkinter module
from tkinter import *
import functools
expression = ""
def press(num):
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
# Try and except statement is used
# for handling the errors like zero

    try:

        global expression
        total = str(eval(expression))

        equation.set(total)
        print(total)
        

# initialize the expression variable
        expression = ""
# if error is generate then handle
# by the except block
    except:

        equation.set(" error ")
        expression = ""

# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

import random
from random import randint
def making_numbers():
    low = ['1','2','3','4','5','6','7','8','9','10']
    big = ['25','50','75','100']
    nob = clicked.get() #number of big
    lob = random.sample(big,nob) #length of big
    lol = random.sample(low,(6-nob)) #length of low
    global numbers
    numbers = [*lol,*lob]
    print(numbers)
    
    operators = ['+','-','*','/']
    
    def press_delete(b, n):
        press(n)
   
       
        def switch():
            if b["state"] == "normal":
                b["state"] = "disabled"
        
            else:
                b["state"] = "normal"

        switch()
        b.grid_forget()
   # def retrieve(b):
    #    for i in range():
     #       buttoni
        
    

    button0 = Button(gui, text=f' {numbers[0]} ', fg='black', bg = 'red',  height=1, width=7)
    button0.configure(command = functools.partial(press_delete, button0, numbers[0]))
    button0.grid(row=2, column=0)


    button1 = Button(gui, text=f' {numbers[1]} ', fg='black', bg = 'red',  height=1, width=7)
    button1.configure(command = functools.partial(press_delete, button1, numbers[1]))
    button1.grid(row=2, column=1)

    button2 = Button(gui, text=f' {numbers[2]} ', fg='black', bg = 'red',  height=1, width=7)
    button2.configure(command = functools.partial(press_delete, button2, numbers[2]))
    button2.grid(row=2, column=2)

    button3 = Button(gui, text=f' {numbers[3]} ', fg='black', bg = 'red',  height=1, width=7)
    button3.configure(command = functools.partial(press_delete, button3, numbers[3]))
    button3.grid(row=3, column=0)

    button4 = Button(gui, text=f' {numbers[4]} ', fg='black', bg = 'red',   height=1, width=7)
    button4.configure(command = functools.partial(press_delete, button4, numbers[4]))
    button4.grid(row=3, column=1)
    
    button5 = Button(gui, text=f' {numbers[5]} ', fg='black', bg = 'red',  height=1, width=7)
    button5.configure(command = functools.partial(press_delete, button5, numbers[5]))
    button5.grid(row=3, column=2)

    
    
    def create_number():
        maths = []
        clone_numbers = numbers.copy()
        for i in range(5):
            n = random.choice(clone_numbers)
            maths.append(n)
            clone_numbers.remove(n)
            o = random.choice(operators)
            maths.append(o)
        maths.append(clone_numbers[0])
        maths.insert(0,'(((((')
        maths.insert(4, ')')
        maths.insert(7,')')
        maths.insert(10,')')
        maths.insert(13,')')
        maths.insert(16,')')
        numans = 0
        #global ans
        ans = ""
        ans = ans.join(maths)
        numans = eval(ans)
        
        while type(numans) != int or numans < 100 or numans > 999:
            ans, numans =create_number()
            if type(numans) == int and numans > 100 and numans < 1000:
                print(numans)
    
        buttontarget = Button(gui, text=f'{numans} ', fg='black', bg='red',
                 height=1, width=7)
        buttontarget.grid(row=4, column=2)
        print(numans)
        
        print(ans)

    create_number()

    
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="white")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("700x500")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    
    def show():
        label.config( text = clicked.get() )
        dropdownsend.destroy()
        print(clicked.get())
    
    nobtions = [
    "1",
    "2",
    "3",
    "4",]
    
    clicked = IntVar()

    # initial menu text
    clicked.set( "Number of Big Numbers" )

    # Create Dropdown menu
    dropdown = OptionMenu( gui , clicked , *nobtions )
    dropdown.grid(row = 2, column = 4)

    # Create button, it will change label text
    dropdownsend = Button( gui , text = "Click to Confirm" , command = show )
    dropdownsend.grid(row = 3, column = 4)

    # Create Label
    label = Label( gui , text = " " )
    

    
    plus = Button(gui, text=' + ', fg='black', bg='red',
        command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',
        command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',
        command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',
        command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',
        command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
        command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    Lbracket = Button(gui, text='(', fg='black', bg='red',
            command=lambda: press('('), height=1, width=7)
    Lbracket.grid(row=6,column=1)
    
    Rbracket = Button(gui, text=')', fg='black', bg='red',
            command=lambda: press(')'), height=1, width=7)
    Rbracket.grid(row=6,column=2)
    
    reset = Button(gui, text = 'Reset', fg = 'black', bg = 'red',
                   command = making_numbers, height = 1, width = 7)
    reset.grid(row = 7, column = 1)
    
    redo = Button(gui, text = 'Redo with same numbers',
                  command = lambda: retrieve(button4))
    redo.grid(row = 7, column = 0)
    
    # start the GUI
    gui.mainloop()
    
making_numbers()     

title = Label(gui, text = "Countdown")
title.grid(row = 1, column = 10)
title.configure(bg = "pink" , font = comicsans, fg = 'white')

bignumbers = Entry(gui, fg = 'black', bg = 'red')
bignumbers.grid(row=7, column = 2)



