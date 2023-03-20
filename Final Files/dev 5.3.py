# imports
import datetime  # Used in the timer
import functools  # Used in buttons that have more than one command
import random  # Used for picking random choices
from random import randint # Used when generating target numbers
import tkinter
from tkinter import StringVar, IntVar, messagebox
import customtkinter as ctk


class HomePage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Countdown Home Page')
        self.geometry(f"{1100}x{450}")
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
    numbers_game = NumbersGame()  # Creates an instance of the NumbersGame class
    numbers_game.mainloop()  # Runs this instance on the mainloop


def make_letters_game():
    letters_game = LettersGame()  # Creates an instance of the LettersGame class
    letters_game.mainloop()  # Runs this instance on the mainloop


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent_app):
        super().__init__(parent_app, width=140, corner_radius=0)

        # Function changes the main colouring to either light or dark mode.
        def change_appearance_mode_event(new_appearance_mode: str):
            ctk.set_appearance_mode(new_appearance_mode)

        # Function changes the scaling of the widgets on the interface.
        def change_scaling_event(new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            ctk.set_widget_scaling(new_scaling_float)

        self.parent_app = parent_app
        # Create sidebar frame with widgets
        # Label to go on Sidebar acting as a sort of title.
        self.logo_label = ctk.CTkLabel(self, text="Countdown", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Button to launch the numbers game.
        self.play_numbers_game = ctk.CTkButton(self, text='Numbers Game', command=make_numbers_game)
        self.play_numbers_game.grid(row=2, column=0, padx=20, pady=10)
        # Button to launch the letters game.
        self.play_letters_game = ctk.CTkButton(self, text='Letters Game', command=make_letters_game)
        self.play_letters_game.grid(row=3, column=0, padx=20, pady=10)
        # Button to change the appearance mode of the GUI.
        self.appearance_mode_label = ctk.CTkLabel(self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=4, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_menu = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                      command=change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=5, column=0, padx=20, pady=(10, 20))
        self.appearance_mode_menu.set("System")
        # Button to change the widget scaling on the GUI.
        self.scaling_label = ctk.CTkLabel(self, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.scaling_menu = ctk.CTkOptionMenu(self,
                                              values=["80%", "90%", "100%", "110%", "120%"],
                                              command=change_scaling_event)
        self.scaling_menu.grid(row=7, column=0, padx=20, pady=(10, 20))
        self.scaling_menu.set("100%")


class Tabview(ctk.CTkFrame):
    # Creating Tabview
    def __init__(self, parent_app):
        super().__init__(parent_app)
        self.parent_app = parent_app

        self.tabview = ctk.CTkTabview(self, width=200)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # Adding the tabview options.
        self.tabview.add("Information about the Game")
        self.tabview.add("How to Play")
        self.tabview.add("About the Developer")
        # Placing the tabview options.
        self.tabview.tab("Information about the Game").grid_columnconfigure(0, weight=1)
        self.tabview.tab("How to Play").grid_columnconfigure(0, weight=1)
        self.tabview.tab("About the Developer").grid_columnconfigure(0, weight=1)

        # Creating Textboxes
        self.textbox_info = ctk.CTkTextbox(self.tabview.tab("Information about the Game"), width=700)
        self.textbox_info.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Reading from the textfile which stores the information about how the game is played.
        with open("Text_files/Information.txt") as file:
            file_contents = file.read()
            self.textbox_info.insert('0.0', file_contents)
        self.textbox_info.configure(state="disabled")

        self.textbox_htp = ctk.CTkTextbox(self.tabview.tab("How to Play"), width=700)
        self.textbox_htp.grid(row=0, column=0, padx=20, pady=(20, 10))
        with open("Text_files/How_To_Play.txt") as file:
            file_contents = file.read()
            self.textbox_htp.insert('0.0', file_contents)
        self.textbox_htp.configure(state="disabled")

        self.textbox_atd = ctk.CTkTextbox(self.tabview.tab("About the Developer"), width=700)
        self.textbox_atd.grid(row=0, column=0, padx=20, pady=(20, 10))
        with open("Text_files/About_The_Developer.txt") as file:
            file_contents = file.read()
            self.textbox_atd.insert('0.0', file_contents)
        self.textbox_atd.configure(state="disabled")


class NumbersGame(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.difference = None
        self.score = IntVar()
        # Input dialog to take the  user's choice for how many big numbers.
        number_of_big = ctk.CTkInputDialog(text="How many big numbers? [1,2,3,4]", title='Big Numbers')
        nob = number_of_big.get_input()

        # Validation of the user's input
        if nob.isdigit():
            nob = int(nob)
            if 0 < nob < 5:
                user_time = ctk.CTkInputDialog(text="""
        How long do you want the timer set for?
        (Enter non integer for unlimited time)
                """, title='Time selection')
                time = user_time.get_input()
                # Validating the user's time input
                if time.isdigit():
                    time = int(time)
                else:
                    time = 0


            # If the data input regarding the number of big numbers is incorrect, the input dialog is deleted and reprompted.
            else:
                ctk.CTkInputDialog.destroy(self)
                make_numbers_game()
        else:
            ctk.CTkInputDialog.destroy(self)
            make_numbers_game()

        self.title('Numbers Game')
        self.SidebarFrame = Sidebar(self)
        self.SidebarFrame.grid(row=0, column=0, rowspan=4,
                               sticky="nsew")  # grid method is used for placing the widgets at respective positions
        self.SidebarFrame.grid_rowconfigure(4, weight=1)

        self.equation = StringVar()  # StringVar() is the variable class we create an instance of this class
        self.expression_field = ctk.CTkEntry(self,
                                             textvariable=self.equation)  # create the text entry box for showing the expression.
        self.expression_field.grid(row=0, column=2, columnspan=4, ipadx=100)
        self.expression_field.configure(state="disabled")

        # Making the big number and developing all possible solutions
        def making():

            big_options = [25, 50, 75, 100]
            small_options = [i for i in range(1, 11)] * 2
            lob = random.sample(big_options, nob)  # big numbers used in number list
            los = random.sample(small_options, (6 - nob))  # small numbers used in number list
            self.numbers = [*los, *lob]
            self.target = randint(100, 999)

        # define a function to generate a list of all solutions
        def solutions_list():
            # initialize an empty list to hold the solutions
            solutions = list()
            # call the solve function to find all solutions
            solve(self.target, self.numbers, list(), solutions)
            # initialize two lists to hold unique and final solutions
            unique = list()
            self.final = list()

            # iterate over all solutions and keep only the unique ones
            for s in solutions:
                # concatenate the elements of the path into a single string and sort it
                a = ''.join(sorted(s))
                if not a in unique:
                    # if the sorted string is not in the unique list, add it to both lists
                    unique.append(a)
                    self.final.append(s)

            # if there are final solutions, choose the one with the shortest length as the best solution
            if self.final:
                self.best_solution = min(self.final, key=len)
                # convert the best solution from a list of strings to a single string separated by newlines
                self.best_solution = '\n'.join(self.best_solution)

            # print the total number of solutions
            print(f"There are a total of {len(self.final)} solutions.")

        # define a recursive function to search for solutions
        def solve(target, numbers, path, solutions):
            # base case: if there is only one number left, there are no more pairs to combine
            if len(numbers) == 1:
                return

            # initialize a list of distinct numbers sorted in descending order
            distinct = sorted(list(set(numbers)), reverse=True)
            # initialize a list of remaining distinct numbers
            remainder = list(distinct)

            # iterate over all distinct pairs of numbers and apply each of the four arithmetic operators
            for n1 in distinct:  # reduce list by combining a pair
                # remove the current value of n1 from the remainder list so it can't be used again
                remainder.remove(n1)
                for n2 in remainder:
                    # create a copy of the numbers list in case of duplicates
                    rem2 = list(numbers)
                    # remove the current pair of numbers (n1, n2) from the copy of the list
                    rem2.remove(n1)
                    rem2.remove(n2)
                    # evaluate the result of applying the current arithmetic operator to the current pair of numbers
                    combine(target, solutions, path, rem2, n1, n2, '+')
                    combine(target, solutions, path, rem2, n1, n2, '-')
                    if n2 > 1:
                        combine(target, solutions, path, rem2, n1, n2, '*')
                        if not n1 % n2:
                            combine(target, solutions, path, rem2, n1, n2, '//')

        # helper function to evaluate the result of applying an arithmetic operator to a pair of numbers
        def combine(target, solutions, path, rem2, n1, n2, symb):
            # create a copy of the remaining numbers list
            lst = list(rem2)
            # evaluate the result of applying the current arithmetic operator to the current pair of numbers
            ans = eval(f"{n1}{symb}{n2}")
            # create a new path string that shows the current operation and its result
            newpath = path + [f"{n1}{symb[0]}{n2}={ans}"]
            # if the result equals the target, add the path to the solutions list
            if ans == target:
                solutions += [newpath]
            else:
                # if the result does not equal the target, add it to the remaining numbers list and recursively call the solve function
                lst.append(ans)
                solve(target, lst, newpath, solutions)

        def display_best_solution():
            best_solution_text = ctk.CTkTextbox(self, height=40, width=150)
            best_solution_text.grid(row=brn + 7, column=3, padx=20, pady=(20, 10))
            best_solution_text.insert('0.0', f'{self.best_solution}')
            best_solution_text.configure(state="disabled")

        def print_all_solutions():
            for s in self.final:  # print them out
                print(s)
            print(f"There are a total of {len(self.final)} solutions.")

        def switch():
            # creates two lists, each list containing each type of button
            # when a button is clicked the state switches to new_state, which is dependent on the button_c which is a constant
            buttons = [buttonc, button0, button1, button2, button3, button4, button5]
            ops = [plus, minus, multiply, divide]
            new_state = "disabled" if buttonc["state"] == "normal" else "normal"
            for button in buttons:
                button.configure(state=new_state)
            for op in ops:
                op.configure(state="normal" if new_state == "disabled" else "disabled")

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
                self.user_total = str(eval(self.expression))
                self.equation.set(self.user_total)
                print(f"Your answer evaluated to {self.user_total}")
                calculate_score()
            # if error is generated then handle by the except block
            except:
                self.equation.set(" error ")

        # Function to calculate score based off target and user's expression.
        def calculate_score():
            self.difference = abs(self.target - float(self.user_total))
            if self.difference == 0:
                self.score.set(self.score.get() + 10)
                score_label.configure(text=f'Score: {self.score.get()}')
                print(f"Number evaluated equalled the target, so you scored {self.score.get()} points")
            elif 0 < self.difference < 6:
                self.score.set(self.score.get() + 7)
                score_label.configure(text=f'Score: {self.score.get()}')
                print(f"Number evaluated is {self.difference} from the target, so you scored {self.score.get()} points")
            elif 6 <= self.difference <= 10:
                self.score.set(self.score.get() + 5)
                score_label.configure(text=f'Score: {self.score.get()}')
                print(f"Number evaluated is {self.difference} from the target, so you scored {self.score.get()} points")
            else:
                print(f"Number evaluated is {self.difference} from the target, so you scored {self.score.get()} points")

        def operand_press_switch(op):
            press(op)
            switch()

        making()
        brn = -1  # base row number
        bcn = 2  # base column number

        target_label = ctk.CTkButton(self, text=f"Target is {self.target}", text_color="red")
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

        plus.configure(state="disabled")
        minus.configure(state="disabled")
        multiply.configure(state="disabled")
        divide.configure(state="disabled")

        equal = ctk.CTkButton(self, text=' = ', command=functools.partial(equalpress))
        equal.grid(row=brn + 6, column=bcn + 2, padx=10, pady=10)

        Lbracket = ctk.CTkButton(self, text='(', command=lambda: press('('))
        Lbracket.grid(row=brn + 5, column=bcn + 1)

        Rbracket = ctk.CTkButton(self, text=')', command=lambda: press(')'))
        Rbracket.grid(row=brn + 5, column=bcn + 2)

        best_solutions = ctk.CTkButton(self, text='Display best solution', command=display_best_solution)
        best_solutions.grid(row=brn + 7, column=bcn + 0)

        best_solutions = ctk.CTkButton(self, text='Print all solutions', command=print_all_solutions)
        best_solutions.grid(row=brn + 7, column=bcn + 2)

        score_label = ctk.CTkLabel(self, text=f'Score: {self.score.get()}')
        score_label.grid(row=brn + 2, column=bcn + 2)

        timer_string_var = ctk.StringVar(self)
        time_b = ctk.CTkButton(self, textvariable=timer_string_var)
        time_b.configure(state="disabled", fg_color='red', text_color_disabled='white')
        time_b.grid(row=brn + 2, column=bcn + 1)


        self.t_seconds = time

        def update_gui2():
            timer = datetime.timedelta(seconds=self.t_seconds)
            timer_string_var.set(timer)
            self.t_seconds -= 1
            if self.t_seconds == 0:
                messagebox.showinfo("Time Countdown", """Time's up!
                You can continue playing this round, but for practise sake, you may continue.
                 """)
                ctk.CTkToplevel.configure(self, state="disabled")
            self.update()
            self.after(1000, update_gui2)

        solutions_list()
        update_gui2()


class LettersGame(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.all_possible = []
        self.longest_words = []
        self.score = IntVar()
        number_of_vowels = ctk.CTkInputDialog(text="How many Vowels? [3,4,5]", title='Vowels')
        nov = number_of_vowels.get_input()
        if nov.isdigit():
            nov = int(nov)
            if 2 < nov < 6:
                user_time = ctk.CTkInputDialog(text="""
        How long do you want the timer set for?
        (Enter non integer for unlimited time)
                                """, title='Time selection')
                time = user_time.get_input()
                if time.isdigit():
                    time = int(time)
                else:
                    time = 0

            else:
                ctk.CTkInputDialog.destroy(self)
                make_letters_game()
        else:
            ctk.CTkInputDialog.destroy(self)
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

            # Next, let's define a list of words that we want to check
            with open('/usr/share/dict/words', 'r') as f:
                words = f.read().split()
                self.filtered_words = [item for item in words if not item[0].isupper()]
                # Removes pronouns from the list of possible words increasing efficiency.

            # Now, we can iterate through the list of words and check if they can be made from the list of letters
            for word in self.filtered_words:
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
            self.user_word = entry.get()
            self.user_word = self.user_word.lower()
            if buttonc["state"] == "normal":
                buttonc.configure(state="disabled")
                submit.configure(state="disabled")
            calculate_score()
        def calculate_score():
            if self.user_word in self.all_possible:
                if len(self.user_word) == 9:
                    self.score.set(
                        self.score.get() + 18)  # 18 comes from wikipedia ruleset, and stating that if all 9 letters are used, the contestant scores 18 points.
                    score_label.configure(text=f'Score: {self.score.get()}')
                else:
                    self.score.set(self.score.get() + len(self.user_word))
                    score_label.configure(text=f'Score: {self.score.get()}')
                print(
                    f"As your word {self.user_word} has a length of {len(self.user_word)} you score {self.score.get()} points")



        def display_best_words():
            best_words_text = ctk.CTkTextbox(self, height=40)
            best_words_text.grid(row=3, column=2, padx=20, pady=(20, 10))
            best_words_text.insert('0.0', f'{self.longest_words}')
            best_words_text.configure(state="disabled")

        def display_all_words():
            self.all_possible_print = '\n'.join(self.all_possible)
            print(self.all_possible_print)
            print(f'There are a total of {len(self.all_possible)} words that can be made.')

        making_letters()
        bcn = 1  # Base column number

        letter0 = ctk.CTkButton(self, text=f' {self.letters[0].upper()} ', font=('arial', 20, 'bold'))
        letter0.configure(state="disabled")
        letter0.grid(row=1, column=bcn, padx=20, pady=5)

        letter1 = ctk.CTkButton(self, text=f' {self.letters[1].upper()} ', font=('arial', 20, 'bold'))
        letter1.configure(state="disabled")
        letter1.grid(row=1, column=bcn + 1, padx=20, pady=5)

        letter2 = ctk.CTkButton(self, text=f' {self.letters[2].upper()} ', font=('arial', 20, 'bold'))
        letter2.configure(state="disabled")
        letter2.grid(row=1, column=bcn + 3, padx=20, pady=5)

        letter3 = ctk.CTkButton(self, text=f' {self.letters[3].upper()} ', font=('arial', 20, 'bold'))
        letter3.configure(state="disabled")
        letter3.grid(row=1, column=bcn + 4, padx=20, pady=5)

        letter4 = ctk.CTkButton(self, text=f' {self.letters[4].upper()} ', font=('arial', 20, 'bold'))
        letter4.configure(state="disabled")
        letter4.grid(row=2, column=bcn + 0, padx=20, pady=5)

        letter5 = ctk.CTkButton(self, text=f' {self.letters[5].upper()} ', font=('arial', 20, 'bold'))
        letter5.configure(state="disabled")
        letter5.grid(row=2, column=bcn + 1, padx=20, pady=5)

        letter6 = ctk.CTkButton(self, text=f' {self.letters[6].upper()} ', font=('arial', 20, 'bold'))
        letter6.configure(state="disabled")
        letter6.grid(row=2, column=bcn + 2)

        letter7 = ctk.CTkButton(self, text=f' {self.letters[7].upper()} ', font=('arial', 20, 'bold'))
        letter7.configure(state="disabled")
        letter7.grid(row=2, column=bcn + 3)

        letter8 = ctk.CTkButton(self, text=f' {self.letters[8].upper()} ', font=('arial', 20, 'bold'))
        letter8.configure(state="disabled")
        letter8.grid(row=2, column=bcn + 4)

        submit = ctk.CTkButton(self, text=' Submit ', command=submitpress)
        submit.grid(row=0, column=3)

        entry = ctk.CTkEntry(self, width=200)
        entry.grid(row=0, column=2)

        best_words = ctk.CTkButton(self, text='Display best words', command=display_best_words)
        best_words.configure(fg_color='red')
        best_words.grid(row=3, column=1)

        all_words = ctk.CTkButton(self, text='Print all words', command=display_all_words)
        all_words.configure(fg_color='red')
        all_words.grid(row=3, column=3)

        score_label = ctk.CTkLabel(self, text=f'Score: {self.score.get()}')
        score_label.grid(row=0, column=1)

        buttonc = tkinter.Button(self, text=f'Constant button')

        timer_string_var = ctk.StringVar(self)
        time_b = ctk.CTkButton(self, textvariable=timer_string_var)
        time_b.configure(state="disabled", fg_color='red', text_color_disabled='white')
        time_b.grid(row=0, column=4)

        self.t_seconds = time

        def update_gui():
            timer = datetime.timedelta(seconds=self.t_seconds)
            timer_string_var.set(timer)
            self.t_seconds -= 1
            if self.t_seconds == 0:
                messagebox.showinfo("Time Countdown", """Time's up!
                You can continue playing this round, but for practise sake, you may continue.
                 """)
                ctk.CTkToplevel.configure(self, state="disabled")
            self.update()
            self.after(1000, update_gui)

        update_gui()

        print(self.letters)


if __name__ == "__main__":
    page = HomePage()
    page.mainloop()
