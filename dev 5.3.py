# imports
import functools
from time import sleep
import random
import tkinter
from random import randint
from tkinter import StringVar, messagebox
import customtkinter as ctk


class HomePage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Countdown Home Page')
        self.geometry(f"{1100}x{580}")
        self.resizable(True, True)
        self.sidebar_frame = Sidebar(self)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.tabview = Tabview(self)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


def make_numbers_game():
    numbers_game = Numbers_Game()
    numbers_game.mainloop()



def make_letters_game():
    letters_game = Letters_Game()
    letters_game.mainloop()

def make_timer():
    timer = Timer()
    timer.mainloop()
    print('pop')


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent_app):
        super().__init__(parent_app, width=140, corner_radius=0)

        def change_appearance_mode_event(new_appearance_mode: str):
            ctk.set_appearance_mode(new_appearance_mode)

        def change_scaling_event(new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            ctk.set_widget_scaling(new_scaling_float)

        def set_timer_event(newtime : str):
            if newtime != "Unlimited":
                self.temp = int(newtime.replace("S",""))
            else:
                self.temp = -1

        self.sidebar_button_event = None

        self.parent_app = parent_app
        # create sidebar frame with widgets
        self.logo_label = ctk.CTkLabel(self, text="Countdown", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self, text='Home', command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.play_numbers_game = ctk.CTkButton(self, text='Numbers Game', command=make_numbers_game)
        self.play_numbers_game.grid(row=2, column=0, padx=20, pady=10)
        self.play_letters_game = ctk.CTkButton(self, text='Letters Game', command=make_letters_game)
        self.play_letters_game.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = ctk.CTkLabel(self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=4, column=0, padx=20, pady=(10,20))
        self.appearance_mode_menu = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                      command=change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=5, column=0, padx=20, pady=(10, 20))
        self.scaling_label = ctk.CTkLabel(self, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.scaling_menu = ctk.CTkOptionMenu(self,
                                              values=["80%", "90%", "100%", "110%", "120%"],
                                              command=change_scaling_event)
        self.scaling_menu.grid(row=7, column=0, padx=20, pady=(10, 20))

        self.second_label = ctk.CTkLabel(self, text="Timer Length:", anchor="w")
        self.second_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.second_menu = ctk.CTkOptionMenu(self,
                                              values=["30s", "60s", "90s", "Unlimited"],
                                              command=set_timer_event)
        self.second_menu.grid(row=9, column=0, padx=20, pady=(10, 20))



class Tabview(ctk.CTkFrame):
    # create tabview
    def __init__(self, parent_app):
        super().__init__(parent_app)
        self.parent_app = parent_app
        self.tabview = ctk.CTkTabview(self, width=200)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Information about the Game")
        self.tabview.add("How to Play")
        self.tabview.add("About the Developer")
        self.tabview.tab("Information about the Game").grid_columnconfigure(0,
                                                                            weight=1)  # configure grid of individual tabs
        self.tabview.tab("How to Play").grid_columnconfigure(0, weight=1)
        self.tabview.tab("About the Developer").grid_columnconfigure(0, weight=1)

        # create textbox
        self.textbox_info = ctk.CTkTextbox(self.tabview.tab("Information about the Game"), width=700)
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
        self.textbox_htp.insert('0.0', """First begin by choosing the preferred option between the Letters Game and the Numbers Game.
        The Numbers Game, will prompt for how many big numbers you want to use then wait for the game to appear.
        First select the first number you want to use and then choose an operation to follow, continue choosing different numbers and different operations
        in aim of reaching the target number and once you've gone through all the operations click the equals sign to lock in your answer and evaluate the answer.
        
        The Letters Game, will prompt for how many vowels you want to use, and the remaining letters will be provided.
        Make the longest word you can using the 9 letters and input it into the box above, before the timer runs out 
        or when you have reached the longest word you can, submit the word.
        """)

        self.textbox_atd = ctk.CTkTextbox(self.tabview.tab("About the Developer"), width=250)
        self.textbox_atd.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.textbox_atd.insert('0.0', 'Hi there')

        # self.login = ctk.CTkButton(self, text="Log in", command=self.log_in)
        # self.login.grid(row=0, column=2, padx=20, pady=20)

        # self.close = ctk.CTkButton(self, text = 'Close', command = self.close)
        # self.login.grid(row=2, column=2, padx=20, pady=20)
        # self.appearance_mode_optionemenu.set("Dark")
        # self.scaling_optionemenu.set("100%")


class Numbers_Game(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.score = None
        self.target = None
        self.best_solution = None
        self.numbers = None
        self.equation = None
        number_of_big = ctk.CTkInputDialog(text="How many big numbers? [1,2,3,4]", title='Big Numbers')
        nob = number_of_big.get_input()
        nob = int(nob)
        if 0 < nob < 5:
            pass
        else:
            number_of_big.destroy()
            make_numbers_game()

        self.title('Numbers Game')
        self.SidebarFrame = Sidebar(self)
        self.SidebarFrame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.SidebarFrame.grid_rowconfigure(4, weight=1)

        self.equation = StringVar()  # StringVar() is the variable class we create an instance of this class
        self.expression_field = ctk.CTkEntry(self,
                                             textvariable=self.equation)  # create the text entry box for showing the
        # expression.
        self.expression_field.grid(row=0, column=2, columnspan=4,
                                   ipadx=100)  # grid method is used for placing the widgets at respective positions

        # in table like structure.

        # Making the big number and developing all possible solutions
        def making():
            self.score = 0
            big_options = [25, 50, 75, 100]
            small_options = [i for i in range(1, 11)] * 2
            # small_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5,Ë 6, 7, 8, 9, 10]
            lob = random.sample(big_options, nob)  # big numbers used in number list
            los = random.sample(small_options, (6 - nob))  # small numbers used in number list
            self.numbers = [*los, *lob]
            self.target = randint(100, 999)

        def solutions_list():
            solutions = list()
            solve(self.target, self.numbers, list(), solutions)
            unique = list()
            self.final = list()
            for s in solutions:
                a = ''.join(sorted(s))
                if not a in unique:
                    unique.append(a)
                    self.final.append(s)
            for s in self.final:  # print them out
                print(s)

            self.best_solution = min(self.final, key=len)

            print(f"There are a total of {len(self.final)} solutions.")

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

        #
        # def solutions_list():
        #     solutions = list()
        #     #solve(self.target, self.numbers, list(), solutions)
        #     pool = multiprocessing.Pool()
        #     args = [(self.target, self.numbers, list(), solutions) for _ in range(multiprocessing.cpu_count())]
        #     pool.starmap(solve, args)
        #
        #     unique = list()
        #     self.final = list()
        #     for s in solutions:
        #         a = ''.join(sorted(s))
        #         if not a in unique:
        #             unique.append(a)
        #             self.final.append(s)
        #     for s in self.final:  # print them out
        #         print(s)
        #
        #     self.best_solution = (min(self.final, key=len))
        #
        #     print(f"There are a total of {len(self.final)} solutions.")
        #
        # def solve(args):
        #     target, numbers, path, solutions = args
        #
        #     if len(numbers) == 1:
        #         return
        #     distinct = sorted(list(set(numbers)), reverse=True)
        #     remainder = list(distinct)
        #     for n1 in distinct:  # reduce list by combining a pair
        #         remainder.remove(n1)
        #         for n2 in remainder:
        #             rem2 = list(
        #                 numbers)  # in case of duplicates we need to start with full list and take out the n1,n2 pair of elements
        #             rem2.remove(n1)
        #             rem2.remove(n2)
        #             combine(target, solutions, path, rem2, n1, n2, '+')
        #             combine(target, solutions, path, rem2, n1, n2, '-')
        #             if n2 > 1:
        #                 combine(target, solutions, path, rem2, n1, n2, '*')
        #                 if not n1 % n2:
        #                     combine(target, solutions, path, rem2, n1, n2, '//')
        #
        #
        # def combine(target, solutions, path, rem2, n1, n2, symb):
        #     lst = list(rem2)
        #     ans = eval("{0}{2}{1}".format(n1, n2, symb))
        #     newpath = path + ["{0}{3}{1}={2}".format(n1, n2, ans, symb[0])]
        #     if ans == target:
        #         solutions += [newpath]
        #     else:
        #         lst.append(ans)
        #         solve_parallel(target, lst, newpath, solutions)

        def display_best_solution():
            best_solution_text = ctk.CTkTextbox(self, height=40)
            best_solution_text.grid(row=brn + 7, column=3, padx=20, pady=(20, 10))
            best_solution_text.insert('0.0', f'{self.best_solution}')

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
                plus.configure(state="disabled")
                minus.configure(state="disabled")
                multiply.configure(state="disabled")
                divide.configure(state="disabled")

        def number_press_delete(b, n):
            press(n)
            switch()
            b.grid_remove()

        # Button initialisation
        # On click of a button, the result enters the expression bar
        self.expression = ""

        def press(num):
            self.expression = self.expression + str(num)  # Concatenation of string
            self.equation.set(self.expression)  # Update the expression by using set method

        # Function to evaluate the final expression
        def equalpress():
            try:  # Try and except statement is used for handling the errors like zero
                self.total = str(eval(self.expression))
                self.equation.set(self.total)
                print(self.total)
                expression = ""  # initialize the expression variable
            # if error is generate then handle by the except block
            except:
                self.equation.set(" error ")
                expression = ""

            difference = abs(self.target - float(self.total))
            if difference == 0:
                self.score += 10
                print(self.score)
            elif difference < 10:
                self.score += 10 - difference
                print(self.score)
            else:
                print("Number evaluated is too far from target to score any points")

        # Function to clear the contents of text entry box
        # def clear():
        #   self.expression = ""
        #  equation.set("")

        def operand_press_switch(op):
            press(op)
            switch()

        def remember():
            if not button1.winfo_viewable():
                button1.grid()

        making()
        brn = -1  # base row number
        bcn = 2

        target_label = ctk.CTkButton(self, text=f"Target is {self.target}", text_color=("red"))
        target_label.configure(state="disabled", fg_color='red', text_color_disabled='white')
        target_label.grid(row=brn + 2, column=bcn + 0, padx=10, pady=10)

        buttonc = tkinter.Button(self, text=f'Constant button')

        button0 = ctk.CTkButton(self, text=f' {self.numbers[0]} ', font=('arial', 20, 'bold'))
        button0.configure(command=functools.partial(number_press_delete, button0, self.numbers[0]))
        button0.grid(row=brn + 3, column=bcn + 0, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text=f' {self.numbers[1]} ', font=('arial', 20, 'bold'))
        button1.configure(command=functools.partial(number_press_delete, button1, self.numbers[1]))
        button1.grid(row=brn + 3, column=bcn + 1, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text=f' {self.numbers[2]} ', font=('arial', 20, 'bold'))
        button2.configure(command=functools.partial(number_press_delete, button2, self.numbers[2]))
        button2.grid(row=brn + 3, column=bcn + 2, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text=f' {self.numbers[3]} ', font=('arial', 20, 'bold'))
        button3.configure(command=functools.partial(number_press_delete, button3, self.numbers[3]))
        button3.grid(row=brn + 4, column=bcn + 0, padx=10, pady=10)

        button4 = ctk.CTkButton(self, text=f' {self.numbers[4]} ', font=('arial', 20, 'bold'))
        button4.configure(command=functools.partial(number_press_delete, button4, self.numbers[4]))
        button4.grid(row=brn + 4, column=bcn + 1, padx=10, pady=10)

        button5 = ctk.CTkButton(self, text=f' {self.numbers[5]} ', font=('arial', 20, 'bold'))
        button5.configure(command=functools.partial(number_press_delete, button5, self.numbers[5]))
        button5.grid(row=brn + 4, column=bcn + 2, padx=10, pady=10)

        # operation buttons
        plus = ctk.CTkButton(self, text=' + ')
        plus.configure(command=functools.partial(operand_press_switch, ' + '))
        plus.grid(row=brn + 3, column=bcn + 3)

        minus = ctk.CTkButton(self, text=' - ')
        minus.configure(command=functools.partial(operand_press_switch, '-'))
        minus.grid(row=brn + 4, column=bcn + 3)

        multiply = ctk.CTkButton(self, text=' * ')
        multiply.configure(command=functools.partial(operand_press_switch, '*'))
        multiply.grid(row=brn + 5, column=bcn + 3)

        divide = ctk.CTkButton(self, text=' / ')
        divide.configure(command=functools.partial(operand_press_switch, '/'))
        divide.grid(row=brn + 6, column=bcn + 3)

        equal = ctk.CTkButton(self, text=' = ', command=equalpress)
        equal.grid(row=brn + 6, column=bcn + 2, padx=10, pady=10)

        # clear = ctk.CTkButton(self, text='Clear', command=clear)
        # clear.grid(row=brn + 5, column='0', padx=10, pady=10)

        undo_button = ctk.CTkButton(self, text='Undo', font=('arial', 20, 'bold'))
        undo_button.configure(command=remember())
        undo_button.grid(row=brn + 6, column=bcn + 0)

        Lbracket = ctk.CTkButton(self, text='(', command=lambda: press('('))
        Lbracket.grid(row=brn + 5, column=bcn + 1)

        Rbracket = ctk.CTkButton(self, text=')', command=lambda: press(')'))
        Rbracket.grid(row=brn + 5, column=bcn + 2)

        best_solutions = ctk.CTkButton(self, text='Display best solutions', command=display_best_solution)
        best_solutions.grid(row=brn + 7, column=bcn + 0)

        timer_string_var = ctk.StringVar(self)
        time_b = ctk.CTkButton(self, textvariable=timer_string_var)
        time_b.configure(state="disabled", fg_color='red', text_color_disabled='white')
        time_b.grid(row=brn + 2, column=bcn + 1)

        t_seconds = 3
        solutions_list()


class Letters_Game(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.all_possible = []
        self.longest_words = []
        self.score = None
        number_of_vowels = ctk.CTkInputDialog(text="How many Vowels? [3,4,5]", title='Vowels')
        nov = number_of_vowels.get_input()
        nov = int(nov)
        if nov < 3 or nov > 5:
            make_letters_game()
        self.title('Letters Game')
        self.Sidebarframe = Sidebar(self)
        self.Sidebarframe.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.Sidebarframe.grid_rowconfigure(4, weight=1)

        def making_letters():
            # First, let's define a list of letters
            consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'W',
                          'Y', 'Z']
            vowels = ['A', 'E', 'I', 'O', 'U']
            vow = random.choices(vowels, weights=(15, 21, 13, 13, 5), k=nov)
            number_of_consonants = 9 - nov
            cons = random.choices(consonants, weights=(2, 3, 6, 2, 3, 2, 1, 1, 5, 4, 8, 4, 1, 9, 9, 9, 1, 1, 1, 1, 1),
                                  k=number_of_consonants)
            self.letters = [ops.lower() for ops in [*vow, *cons]]

            # self.all_possible = []
            # Next, let's define a list of words that we want to check
            with open('/usr/share/dict/words', 'r') as f:
                self.words = f.read().split()

            self.score = 0

            # Now, we can iterate through the list of words and check if they can be made from the list of letters
            for word in self.words:
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
            longest_words_h = [word for word in self.all_possible if len(word) == max_length]
            self.longest_words = '\n'.join(longest_words_h)

            # Print the longest words

        def submitpress():
            self.total = entry.get()
            print(self.total)
            if self.total in self.all_possible:
                self.score += len(self.total)
                print(self.score)

            if buttonc["state"] == "normal":
                buttonc.configure(state="disabled")
                submit.configure(state="disabled")

        def display_best_words():
            best_words_text = ctk.CTkTextbox(self, height=40)
            best_words_text.grid(row=3, column=2, padx=20, pady=(20, 10))
            best_words_text.insert('0.0', f'{self.longest_words}')

        def display_all_words():
            all_words_text = ctk.CTkTextbox(self, height=40)
            all_words_text.grid(row=3, column=4, padx=20, pady=(20, 10))
            all_words_text.insert('0.0', f'{self.all_possible}')

        making_letters()
        bcn = 1  # Base column number

        letter0 = ctk.CTkButton(self, text=f' {self.letters[0]} ', font=('arial', 20, 'bold'))
        letter0.configure(state="disabled")
        letter0.grid(row=1, column=bcn, padx=20, pady=5)

        letter1 = ctk.CTkButton(self, text=f' {self.letters[1]} ', font=('arial', 20, 'bold'))
        letter1.configure(state="disabled")
        letter1.grid(row=1, column=bcn + 1, padx=20, pady=5)

        letter2 = ctk.CTkButton(self, text=f' {self.letters[2]} ', font=('arial', 20, 'bold'))
        letter2.configure(state="disabled")
        letter2.grid(row=1, column=bcn + 3, padx=20, pady=5)

        letter3 = ctk.CTkButton(self, text=f' {self.letters[3]} ', font=('arial', 20, 'bold'))
        letter3.configure(state="disabled")
        letter3.grid(row=1, column=bcn + 4, padx=20, pady=5)

        letter4 = ctk.CTkButton(self, text=f' {self.letters[4]} ', font=('arial', 20, 'bold'))
        letter4.configure(state="disabled")
        letter4.grid(row=2, column=bcn + 0, padx=20, pady=5)

        letter5 = ctk.CTkButton(self, text=f' {self.letters[5]} ', font=('arial', 20, 'bold'))
        letter5.configure(state="disabled")
        letter5.grid(row=2, column=bcn + 1, padx=20, pady=5)

        letter6 = ctk.CTkButton(self, text=f' {self.letters[6]} ', font=('arial', 20, 'bold'))
        letter6.configure(state="disabled")
        letter6.grid(row=2, column=bcn + 2)

        letter7 = ctk.CTkButton(self, text=f' {self.letters[7]} ', font=('arial', 20, 'bold'))
        letter7.configure(state="disabled")
        letter7.grid(row=2, column=bcn + 3)

        letter8 = ctk.CTkButton(self, text=f' {self.letters[8]} ', font=('arial', 20, 'bold'))
        letter8.configure(state="disabled")
        letter8.grid(row=2, column=bcn + 4)

        submit = ctk.CTkButton(self, text=' Submit ', command=submitpress)
        submit.grid(row=0, column=4)

        entry = ctk.CTkEntry(self, width=200)
        entry.grid(row=0, column=2)

        best_words = ctk.CTkButton(self, text='Display best words', command=display_best_words)
        best_words.grid(row=3, column=1)

        all_words = ctk.CTkButton(self, text='Display all words', command=display_all_words)
        all_words.grid(row=3, column=3)

        score_label = ctk.CTkLabel(self, text=f'Score: {self.score}')
        score_label.grid(row=0, column=1)

        buttonc = tkinter.Button(self, text=f'Constant button')


class Timer(ctk.CTkToplevel):
    def __init__(self, parent_app):
        self.temp = newtime
        self.title("Time Counter")
        self.geometry("300x250")
        self.time = ctk.CTkLabel(self, text="")
        second = StringVar()
        second.set("00")
        secondLabel = ctk.CTkLabel(self, width=5, font=('Arial', 18), textvariable=second)
        secondLabel.place(x=130, y=30)

        while self.temp > -1:

            # divmod(firstvalue = temp//60, secondvalue = temp%60)

            second.set("{0:2d}".format(self.temp))

            # updating the GUI window after decrementing the
            # temp value every time
            self.update()
            sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (self.temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")

            # after every one sec the value of temp will be decremented
            # by one
            self.temp -= 1




if __name__ == "__main__":
    make_timer()
    page = HomePage()
    page.mainloop()

