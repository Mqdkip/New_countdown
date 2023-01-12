from datetime import datetime
#todo REDO THIS --> As you have all words, just make an entry and display the letters and make it work that way, check word inputted against all possible words and if it works then award points.



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


def submitpress():
        global score
        total = entry.get()
        print(total)
        if total in all_possible:
            score += len(total)
            print(score)

        if buttonc["state"] == "normal":
                buttonc.configure(state="disabled")
                submit.configure(state = "disabled")


if __name__ == "__main__":
    gui = ctk.CTk()  # create a GUI window
    gui.configure(background="black")  # set the background colour of GUI window
    gui.title("Countdown Letters")  # set the title of GUI window
    making_letters()
bcn = 0 #Base column number

letter0 = ctk.CTkButton(gui, text=f' {letters[0]} ', font=('arial', 20, 'bold'))
letter0.configure(state = "disabled")
letter0.grid(row=1, column=bcn)

letter1 = ctk.CTkButton(gui, text=f' {letters[1]} ', font=('arial', 20, 'bold'))
letter1.configure(state = "disabled")
letter1.grid(row=1, column=bcn+1)

letter2 = ctk.CTkButton(gui, text=f' {letters[2]} ', font=('arial', 20, 'bold'))
letter2.configure(state = "disabled")
letter2.grid(row=1, column=bcn+2)

letter3 = ctk.CTkButton(gui, text=f' {letters[3]} ', font=('arial', 20, 'bold'))
letter3.configure(state = "disabled")
letter3.grid(row=1, column=bcn+3)

letter4 = ctk.CTkButton(gui, text=f' {letters[4]} ', font=('arial', 20, 'bold'))
letter4.configure(state = "disabled")
letter4.grid(row=1, column=bcn+4)

letter5 = ctk.CTkButton(gui, text=f' {letters[5]} ', font=('arial', 20, 'bold'))
letter5.configure(state = "disabled")
letter5.grid(row=1, column=bcn+5)

letter6 = ctk.CTkButton(gui, text=f' {letters[6]} ', font=('arial', 20, 'bold'))
letter6.configure(state = "disabled")
letter6.grid(row=1, column=bcn+6)

letter7 = ctk.CTkButton(gui, text=f' {letters[7]} ', font=('arial', 20, 'bold'))
letter7.configure(state = "disabled")
letter7.grid(row=1, column=bcn+7)

letter8 = ctk.CTkButton(gui, text=f' {letters[8]} ', font=('arial', 20, 'bold'))
letter8.configure(state = "disabled")
letter8.grid(row=1, column=bcn+8)

submit = ctk.CTkButton(gui, text=' Submit ', command=submitpress)
submit.grid(row=0, column=4)

entry = ctk.CTkEntry(gui)
entry.grid(row = 0, column = 3 )

buttonc = Button(gui, text=f'Constant button')


vowels_label = ctk.CTkLabel(gui, text="vowels:", anchor="w")
vowels_label.grid(row=5, column=0, padx=20, pady=(10, 0))
vowels_optionmenu = ctk.CTkOptionMenu(gui, values = ['3','4','5'])
vowels_optionmenu.grid(row = 6, column = 0)
print(vowels_optionmenu.get())

gui.mainloop()

