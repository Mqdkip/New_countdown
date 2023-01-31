import functools  # import functools for button commands
import random
from random import randint  # import random and randint for sampling and number choice.
import datetime
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.nov = None
        self.geometry(f"{1100}x{580}")
        self.title("Countdown")
        self.resizable(True, True)
        self.sidebar_frame = Sidebar(self)
        # self.tabview = Tabview(self)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

    def run_letters_game(self):
        number_of_vowels = ctk.CTkInputDialog(text="How many Vowels? [3,4,5]", title='Vowels')
        nov = number_of_vowels.get_input()
        self.nov = int(nov)
        if nov < 3 or nov > 5:
            self.run_letters_game()
        gui = ctk.CTkToplevel(self)
        gui.geometry('1000x200')
        gui.configure(background="black")  # set the background colour of GUI window
        gui.title("Countdown Letters")  # set the title of GUI window

    def making_letters(self):
        # First, let's define a list of letters
        consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'W',
                      'Y', 'Z']
        vowels = ['A', 'E', 'I', 'O', 'U']
        vow = random.choices(vowels, weights=(15, 21, 13, 13, 5), k=self.nov)
        number_of_consonants = 9 - self.nov
        cons = random.choices(consonants, weights=(2, 3, 6, 2, 3, 2, 1, 1, 5, 4, 8, 4, 1, 9, 9, 9, 1, 1, 1, 1, 1),
                              k=number_of_consonants)
        global letters
        letters = [ops.lower() for ops in [*vow, *cons]]

        global all_possible
        all_possible = []
        # Next, let's define a list of words that we want to check
        with open('/usr/share/dict/words', 'r') as f:
            words = f.read().split()
        global score
        score = 0

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

        # Find the maximum length of the words
        max_length = max(len(word) for word in all_possible)

        # Use a list comprehension to find the longest words
        global longest_words
        longest_words = [word for word in all_possible if len(word) == max_length]

        # Print the longest words

    def submitpress():
        global score
        global total
        total = entry.get()
        print(total)
        if total in all_possible:
            score += len(total)
            print(score)

        if buttonc["state"] == "normal":
            buttonc.configure(state="disabled")
            submit.configure(state="disabled")

    def display_best_words():
        best_words_text = ctk.CTkTextbox(gui, height=40)
        best_words_text.grid(row=3, column=2, padx=20, pady=(20, 10))
        best_words_text.insert('0.0', f'{longest_words}')

    def display_all_words():
        all_words_text = ctk.CTkTextbox(gui, height=40)
        all_words_text.grid(row=3, column=4, padx=20, pady=(20, 10))
        all_words_text.insert('0.0', f'{all_possible}')

    making_letters(App)
    bcn = 1  # Base column number

    letter0 = ctk.CTkButton(gui, text=f' {letters[0]} ', font=('arial', 20, 'bold'))
    letter0.configure(state="disabled")
    letter0.grid(row=1, column=bcn, padx=20, pady=5)

    letter1 = ctk.CTkButton(gui, text=f' {letters[1]} ', font=('arial', 20, 'bold'))
    letter1.configure(state="disabled")
    letter1.grid(row=1, column=bcn + 1, padx=20, pady=5)

    letter2 = ctk.CTkButton(gui, text=f' {letters[2]} ', font=('arial', 20, 'bold'))
    letter2.configure(state="disabled")
    letter2.grid(row=1, column=bcn + 3, padx=20, pady=5)

    letter3 = ctk.CTkButton(gui, text=f' {letters[3]} ', font=('arial', 20, 'bold'))
    letter3.configure(state="disabled")
    letter3.grid(row=1, column=bcn + 4, padx=20, pady=5)

    letter4 = ctk.CTkButton(gui, text=f' {letters[4]} ', font=('arial', 20, 'bold'))
    letter4.configure(state="disabled")
    letter4.grid(row=2, column=bcn + 0, padx=20, pady=5)

    letter5 = ctk.CTkButton(gui, text=f' {letters[5]} ', font=('arial', 20, 'bold'))
    letter5.configure(state="disabled")
    letter5.grid(row=2, column=bcn + 1, padx=20, pady=5)

    letter6 = ctk.CTkButton(gui, text=f' {letters[6]} ', font=('arial', 20, 'bold'))
    letter6.configure(state="disabled")
    letter6.grid(row=2, column=bcn + 2)

    letter7 = ctk.CTkButton(gui, text=f' {letters[7]} ', font=('arial', 20, 'bold'))
    letter7.configure(state="disabled")
    letter7.grid(row=2, column=bcn + 3)

    letter8 = ctk.CTkButton(gui, text=f' {letters[8]} ', font=('arial', 20, 'bold'))
    letter8.configure(state="disabled")
    letter8.grid(row=2, column=bcn + 4)

    submit = ctk.CTkButton(gui, text=' Submit ', command=submitpress)
    submit.grid(row=0, column=4)

    entry = ctk.CTkEntry(gui, width=200)
    entry.grid(row=0, column=2)

    best_words = ctk.CTkButton(gui, text='Display best words', command=display_best_words)
    best_words.grid(row=3, column=1)

    all_words = ctk.CTkButton(gui, text='Display all words', command=display_all_words)
    all_words.grid(row=3, column=3)

    score_label = ctk.CTkLabel(gui, text=f'Score: {score}')
    score_label.grid(row=0, column=0)

    buttonc = Button(gui, text=f'Constant button')
class Sidebar(ctk.CTkFrame):
    def __init__(self, parent_app):
        super().__init__(parent_app, width=140, corner_radius=0)
        self.change_scaling_event = None
        self.change_appearance_mode_event = None
        self.run_letters_game = None
        #me when th eme me the when the me and the me
        self.sidebar_button_event = None
        self.parent_app = parent_app
        # create sidebar frame with widgets
        self.logo_label = ctk.CTkLabel(self, text="Countdown",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self, text='Home', command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.play_numbers_game = ctk.CTkButton(self, text='Numbers Game',
                                               command=parent_app.run_numbers_game)
        self.play_numbers_game.grid(row=2, column=0, padx=20, pady=10)
        self.play_letters_game = ctk.CTkButton(self, text='Letters Game',
                                               command=self.run_letters_game)
        self.play_letters_game.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = ctk.CTkLabel(self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self,
                                                     values=["80%", "90%", "100%", "110%", "120%"],
                                                     command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

class tabview(ctk.CTkTabview):
    def __init__(self, parent_app):
            # create tabview
            self.appearance_mode_optionemenu = None
            self.scaling_optionemenu = None
            self.parent_app = parent_app
            self.tabview = ctk.CTkTabview(self, width=250)
            self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
            self.tabview.add("Information about the Game")
            self.tabview.add("How to Play")
            self.tabview.add("About the Developer")
            self.tabview.tab("Information about the Game").grid_columnconfigure(0,
                                                                                weight=1)  # configure grid of individual tabs
            self.tabview.tab("How to Play").grid_columnconfigure(0, weight=1)
            self.tabview.tab("About the Developer").grid_columnconfigure(0, weight=1)

            # create textbox
            self.textbox_info = ctk.CTkTextbox(self.tabview.tab("Information about the Game"), width=900)
            self.textbox_info.grid(row=0, column=0, padx=20, pady=(20, 10))
            self.textbox_info.insert('0.0', """
            Countdown is a popular television show game which has been aired since 1982. 
            The game has three sections: Letters, Numbers and Conundrum.

            The letters version provides 9 letters of which the player can choose either 3,4 or 5 vowels
            and the remaining letters to be consonants.
            From these 9 characters, the aim is to make the longest word possible within the time frame.

            The numbers version is similar, the user is prompted to pick the amount of 'big numbers',
            with a maximum of 4 and the remaining numbers are 'small numbers'.
            Provided with these numbers, a target number is provided and the user's aim is to reach this
            target number or as close to as possible within the time frame.

            Conundrum, is the final version where a 9 letter anagram is provided and the aim is to find
            the 9 letter word from this. 
            """)

            self.textbox_htp = ctk.CTkTextbox(self.tabview.tab("How to Play"), width=250)
            self.textbox_htp.grid(row=0, column=0, padx=20, pady=(20, 10))
            self.textbox_htp.insert('0.0', 'Hi there')

            self.textbox_atd = ctk.CTkTextbox(self.tabview.tab("About the Developer"), width=250)
            self.textbox_atd.grid(row=0, column=0, padx=20, pady=(20, 10))
            self.textbox_atd.insert('0.0', 'Hi there')

            self.login = ctk.CTkButton(self, text="Log in", command=self.log_in)
            self.login.grid(row=0, column=2, padx=20, pady=20)

            # self.close = ctk.CTkButton(self, text = 'Close', command = self.close)
            self.login.grid(row=2, column=2, padx=20, pady=20)
            self.appearance_mode_optionemenu.set("Dark")
            self.scaling_optionemenu.set("100%")


if __name__ == "__main__":
    app = App()

    app.mainloop()
