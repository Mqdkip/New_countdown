from datetime import datetime

from tkinter import *  # import everything from tkinter module
from tkinter import messagebox
import customtkinter as ctk
import functools  # import functools for button commands
import random
from random import randint  # import random and randint for sampling and number choice.

def making_letters():
    # First, let's define a list of letters
    import random
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'W', 'Y',
                  'Z']
    vowels = ['A', 'E', 'I', 'O', 'U']
    number_of_vowels = int(input("How many vowels do you want? [3,4,5]"))
    if number_of_vowels > 5 or number_of_vowels < 3:
        print("Number of vowels must be between 3 and 5 inclusive")
        number_of_vowels = int(input("How many vowels do you want? [3,4,5]"))
    vow = random.choices(vowels, weights=(15, 21, 13, 13, 5), k=number_of_vowels)
    number_of_consonants = 9 - number_of_vowels
    cons = random.choices(consonants, weights=(2, 3, 6, 2, 3, 2, 1, 1, 5, 4, 8, 4, 1, 9, 9, 9, 1, 1, 1, 1, 1),
                          k=number_of_consonants)
    global letters
    letters = [ops.lower() for ops in [*vow, *cons]]
    print(letters)
    global all_possible
    all_possible = []
    # Next, let's define a list of words that we want to check
    with open('/usr/share/dict/words', 'r') as f:
        words = f.read().split()
    word = input("Input word using letters in the list provided")
    global score
    score = 0
    if word in words:
        score += len(word)
        print(score)

    # Now, we can iterate through the list of words and check if they can be made from the list of letters
    for word in words:
        remaining_letters = letters[:]
        can_make_word = True

        # Iterate through the letters in the word
        for letter in word:
            # Check if the letter is in the remaining letters list
            if letter in remaining_letters:
                # If it is, remove the letter from the list
                remaining_letters.remove(letter)
            else:
                # If the letter is not in the remaining letters list, we can't make the word
                can_make_word = False
                break

        # Print the result
        if can_make_word:
            all_possible.append(word)
    print(all_possible)

    # Find the maximum length of the words
    max_length = max(len(word) for word in all_possible)

    # Use a list comprehension to find the longest words
    longest_words = [word for word in all_possible if len(word) == max_length]

    # Print the longest words
    print(f"The longest words are: {longest_words}")

expression = ""


def press(num):
    global expression
    expression = expression + str(num)  # Concatenation of string
    equation.set(expression)  # Update the expression by using set method

def letter_press_delete(l, n):
    press(n)
    l.grid_remove()

def submitpress():
        try:  # Try and except statement is used for handling the errors like zero
            global expression
            total = str(expression)
            equation.set(total)
            print(total)
            expression = ""  # initialize the expression variable
        # if error is generate then handle by the except block
        except:
            equation.set(" error ")
            expression = ""

        if total in all_possible:
            score += len(total)
            print(score)


if __name__ == "__main__":
    gui = ctk.CTk()  # create a GUI window
    gui.configure(background="black")  # set the background colour of GUI window
    gui.title("Countdown Letters")  # set the title of GUI window
    equation = StringVar()  # StringVar() is the variable class we create an instance of this class
    expression_field = Entry(gui, textvariable=equation)  # create the text entry box for showing the expression.
    expression_field.grid(columnspan=4,
                          ipadx=100)  # grid method is used for placing the widgets at respective positions in table like structure.
    making_letters()
bcn = 0 #Base column number

letter0 = ctk.CTkButton(gui, text=f' {letters[0]} ', font=('arial', 20, 'bold'))
letter0.configure(command=functools.partial(letter_press_delete, letter0, letters[0]))
letter0.grid(row=1, column=bcn)

letter1 = ctk.CTkButton(gui, text=f' {letters[1]} ', font=('arial', 20, 'bold'))
letter1.configure(command=functools.partial(letter_press_delete, letter1, letters[1]))
letter1.grid(row=1, column=bcn+1)

letter2 = ctk.CTkButton(gui, text=f' {letters[2]} ', font=('arial', 20, 'bold'))
letter2.configure(command=functools.partial(letter_press_delete, letter2, letters[2]))
letter2.grid(row=1, column=bcn+2)

letter3 = ctk.CTkButton(gui, text=f' {letters[3]} ', font=('arial', 20, 'bold'))
letter3.configure(command=functools.partial(letter_press_delete, letter3, letters[3]))
letter3.grid(row=1, column=bcn+3)

letter4 = ctk.CTkButton(gui, text=f' {letters[4]} ', font=('arial', 20, 'bold'))
letter4.configure(command=functools.partial(letter_press_delete, letter4, letters[4]))
letter4.grid(row=1, column=bcn+4)

letter5 = ctk.CTkButton(gui, text=f' {letters[5]} ', font=('arial', 20, 'bold'))
letter5.configure(command=functools.partial(letter_press_delete, letter5, letters[5]))
letter5.grid(row=1, column=bcn+5)

letter6 = ctk.CTkButton(gui, text=f' {letters[6]} ', font=('arial', 20, 'bold'))
letter6.configure(command=functools.partial(letter_press_delete, letter6, letters[6]))
letter6.grid(row=1, column=bcn+6)

letter7 = ctk.CTkButton(gui, text=f' {letters[7]} ', font=('arial', 20, 'bold'))
letter7.configure(command=functools.partial(letter_press_delete, letter7, letters[7]))
letter7.grid(row=1, column=bcn+7)

letter8 = ctk.CTkButton(gui, text=f' {letters[8]} ', font=('arial', 20, 'bold'))
letter8.configure(command=functools.partial(letter_press_delete, letter8, letters[8]))
letter8.grid(row=1, column=bcn+8)

submit = ctk.CTkButton(gui, text=' Submit ', command=submitpress)
submit.grid(row=0, column=4)

gui.mainloop()

