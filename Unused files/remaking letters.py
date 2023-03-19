import random
from tkinter import *
import customtkinter as ctk


class WordMaker:
    def __init__(self, nov):
        self.nov = nov
        self.letters = []
        self.all_possible = []
        self.score = 0
        self.longest_words = []
        self.gui = ctk.CTkToplevel(self)
        self.gui.geometry('1000x200')
        self.gui.configure(background="black")  # set the background colour of GUI window
        self.gui.title("Countdown Letters")  # set the title of GUI window

    def making_letters(self):
        # First, let's define a list of letters
        self.letters = []
        consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'W',
                      'Y', 'Z']
        vowels = ['A', 'E', 'I', 'O', 'U']
        vow = random.choices(vowels, weights=(15, 21, 13, 13, 5), k=self.nov)
        number_of_consonants = 9 - self.nov
        cons = random.choices(consonants, weights=(2, 3, 6, 2, 3, 2, 1, 1, 5, 4, 8, 4, 1, 9, 9, 9, 1, 1, 1, 1, 1),
                              k=number_of_consonants)
        self.letters = [ops.lower() for ops in [*vow, *cons]]

        self.all_possible = []
        # Next, let's define a list of words that we want to check
        with open('/usr/share/dict/words', 'r') as f:
            words = f.read().split()
        self.score = 0

        # Now, we can iterate through the list of words and check if they can be made from the list of letters
        for word in words:
            remaining_letters = self.letters[:]
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
                self.all_possible.append(word)

        # Find the maximum length of the words
        max_length = max(len(word) for word in self.all_possible)

        # Use a list comprehension to find the longest words
        self.longest_words = [word for word in self.all_possible if len(word) == max_length]
        print(self.longest_words)

        bcn = 1  # Base column number

        letter0 = ctk.CTkButton(self.gui, text=f' {self.letters[0]} ', font=('arial', 20, 'bold'))
        letter0.configure(state="disabled")
        letter0.grid(row=1, column=bcn, padx=20, pady=5)

        letter1 = ctk.CTkButton(self.gui, text=f' {self.letters[1]} ', font=('arial', 20, 'bold'))
        letter1.configure(state="disabled")
        letter1.grid(row=1, column=bcn + 1, padx=20, pady=5)

        letter2 = ctk.CTkButton(self.gui, text=f' {self.letters[2]} ', font=('arial', 20, 'bold'))
        letter2.configure(state="disabled")
        letter2.grid(row=1, column=bcn + 3, padx=20, pady=5)

        letter3 = ctk.CTkButton(self.gui, text=f' {self.letters[3]} ', font=('arial', 20, 'bold'))
        letter3.configure(state="disabled")
        letter3.grid(row=1, column=bcn + 4, padx=20, pady=5)

        letter4 = ctk.CTkButton(self.gui, text=f' {self.letters[4]} ', font=('arial', 20, 'bold'))
        letter4.configure(state="disabled")
        letter4.grid(row=2, column=bcn + 0, padx=20, pady=5)

        letter5 = ctk.CTkButton(self.gui, text=f' {self.letters[5]} ', font=('arial', 20, 'bold'))
        letter5.configure(state="disabled")
        letter5.grid(row=2, column=bcn + 1, padx=20, pady=5)

        letter6 = ctk.CTkButton(self.gui, text=f' {self.letters[6]} ', font=('arial', 20, 'bold'))
        letter6.configure(state="disabled")
        letter6.grid(row=2, column=bcn + 2)

        letter7 = ctk.CTkButton(self.gui, text=f' {self.letters[7]} ', font=('arial', 20, 'bold'))
        letter7.configure(state="disabled")
        letter7.grid(row=2, column=bcn + 3)

        letter8 = ctk.CTkButton(self.gui, text=f' {self.letters[8]} ', font=('arial', 20, 'bold'))
        letter8.configure(state="disabled")
        letter8.grid(row=2, column=bcn + 4)

        submit = ctk.CTkButton(self.gui, text=' Submit ', command=self.submitpress)
        submit.grid(row=0, column=4)

        entry = ctk.CTkEntry(self.gui, width=200)
        entry.grid(row=0, column=2)

        best_words = ctk.CTkButton(self.gui, text='Display best words', command=self.display_best_words)
        best_words.grid(row=3, column=1)

        all_words = ctk.CTkButton(self.gui, text='Display all words', command=self.display_all_words)
        all_words.grid(row=3, column=3)

        score_label = ctk.CTkLabel(self.gui, text=f'Score: {self.score}')
        score_label.grid(row=0, column=0)

        buttonc = Button(self.gui, text=f'Constant button')

    def submit_press(self):
        total = self.entry.get()
        print(total)
        # if total in self.all_possible:
        #   score += len(total)
        #  print(score)

        if self.buttonc["state"] == "normal":
            self.buttonc.configure(state="disabled")
            self.submit.configure(state="disabled")

    def display_best_words(self):
        best_words_text = ctk.CTkTextbox(self.gui, height=40)
        best_words_text.grid(row=3, column=2, padx=20, pady=(20, 10))
        best_words_text.insert('0.0', f'{self.longest_words}')

    def display_all_words(self):
        all_words_text = ctk.CTkTextbox(self.gui, height=40)
        all_words_text.grid(row=3, column=4, padx=20, pady=(20, 10))
        all_words_text.insert('0.0', f'{self.all_possible}')


a = WordMaker(3)
a.making_letters()  # Play the game
