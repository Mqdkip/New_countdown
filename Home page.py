#todo get letter's game timer to work
#todo implement numbers game

# todo Undo button
from datetime import datetime
import functools  # import functools for button commands
from random import randint  # import random and randint for sampling and number choice.

import datetime
from tkinter import messagebox

import customtkinter as ctk
from tkinter import *
import random
import csv
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window


        self.title("Countdown")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Countdown", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text = 'Home', command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.play_numbers_game = ctk.CTkButton(self.sidebar_frame, text = 'Numbers Game', command=self.run_numbers_game)
        self.play_numbers_game.grid(row=2, column=0, padx=20, pady=10)
        self.play_letters_game = ctk.CTkButton(self.sidebar_frame, text = 'Letters Game', command=self.run_letters_game)
        self.play_letters_game.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button


        # create tabview
        self.tabview = ctk.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Information about the Game")
        self.tabview.add("How to Play")
        self.tabview.add("About the Developer")
        self.tabview.tab("Information about the Game").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("How to Play").grid_columnconfigure(0, weight=1)
        self.tabview.tab("About the Developer").grid_columnconfigure(0, weight=1)

        # create textbox
        self.textbox_info = ctk.CTkTextbox(self.tabview.tab("Information about the Game"), width=900)
        self.textbox_info.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.textbox_info.insert('0.0',"""
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
        self.login.grid(row = 0, column = 2, padx = 20, pady = 20)

        #self.close = ctk.CTkButton(self, text = 'Close', command = self.close)
        self.login.grid(row=2, column=2, padx=20, pady=20)
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")


    def log_in(self):
        Password = ctk.CTkInputDialog(text="Password:", title="Log in")
        Username = ctk.CTkInputDialog(text="Username:", title="Log in")
        print(Username.get_input(), Password.get_input())

        global file
        file = open('accounts.csv', 'r')
        for line in file:
            item = line.split(',')
            if Username == item[0] and Password == item[1]:
                print('Logged in successfully!')
            else:
                file = open('accounts.csv', 'a')
                info = '\n' + Username + ',' + Password
                file.write(info)
                print('You have been signed up as a log in could not be found')

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


    def run_numbers_game(self):
        number_of_big = ctk.CTkInputDialog(text = "How many big numbers? [1,2,3,4]", title = 'Big Numbers')
        nob = number_of_big.get_input()
        nob = int(nob)
        if nob < 1 or nob > 4:
            self.run_numbers_game()
        gui2 = ctk.CTkToplevel(self)
        gui2.configure(background="black")  # set the background colour of GUI window
        gui2.title("Countdown Numbers")

        equation = StringVar()  # StringVar() is the variable class we create an instance of this class
        expression_field = Entry(gui2, textvariable=equation)  # create the text entry box for showing the expression.
        expression_field.grid(columnspan=4,ipadx=100)  # grid method is used for placing the widgets at respective positions in table like structure.

        # Making the big number and developing all possible solutions
        def making():
            global score
            score = 0
            big_options = [25, 50, 75, 100]
            small_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            lob = random.sample(big_options, nob)  # big numbers used in number list
            los = random.sample(small_options, (6 - nob))  # small numbers used in number list
            global numbers
            numbers = [*los, *lob]
            global target
            target = randint(100, 999)

        def solutions_list():
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
                print(s)
            print(f"There are a total of {len(final)} solutions.")

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

            difference = abs(target - float(total))
            if difference == 0:
                score += 10
                print(score)
            elif difference < 10:
                score += 10 - difference
                print(score)
            else:
                print("Number evaluated is too far from target to score any points")

        # Function to clear the contents of text entry box
        def clear():
            global expression
            expression = ""
            equation.set("")

        def operand_press_switch(op):
            press(op)
            switch()

        def remember():
            if not button1.winfo_viewable():
                button1.grid()

        making()
        brn = 0  # base row number

        target_label = ctk.CTkButton(gui2, text=f"Target is {target}", text_color=("red"))
        target_label.configure(state="disabled", fg_color='red', text_color_disabled='white')
        target_label.grid(row=brn + 1, column=0, padx=10, pady=10)

        buttonc = Button(gui2, text=f'Constant button')

        button0 = ctk.CTkButton(gui2, text=f' {numbers[0]} ', font=('arial', 20, 'bold'))
        button0.configure(command=functools.partial(number_press_delete, button0, numbers[0]))
        button0.grid(row=brn + 3, column=0, padx=10, pady=10)

        button1 = ctk.CTkButton(gui2, text=f' {numbers[1]} ', font=('arial', 20, 'bold'))
        button1.configure(command=functools.partial(number_press_delete, button1, numbers[1]))
        button1.grid(row=brn + 3, column=1, padx=10, pady=10)

        button2 = ctk.CTkButton(gui2, text=f' {numbers[2]} ', font=('arial', 20, 'bold'))
        button2.configure(command=functools.partial(number_press_delete, button2, numbers[2]))
        button2.grid(row=brn + 3, column=2, padx=10, pady=10)

        button3 = ctk.CTkButton(gui2, text=f' {numbers[3]} ', font=('arial', 20, 'bold'))
        button3.configure(command=functools.partial(number_press_delete, button3, numbers[3]))
        button3.grid(row=brn + 4, column=0, padx=10, pady=10)

        button4 = ctk.CTkButton(gui2, text=f' {numbers[4]} ', font=('arial', 20, 'bold'))
        button4.configure(command=functools.partial(number_press_delete, button4, numbers[4]))
        button4.grid(row=brn + 4, column=1, padx=10, pady=10)

        button5 = ctk.CTkButton(gui2, text=f' {numbers[5]} ', font=('arial', 20, 'bold'))
        button5.configure(command=functools.partial(number_press_delete, button5, numbers[5]))
        button5.grid(row=brn + 4, column=2, padx=10, pady=10)

        # operation buttons
        plus = ctk.CTkButton(gui2, text=' + ')
        plus.configure(command=functools.partial(operand_press_switch, ' + '))
        plus.grid(row=brn + 3, column=3)

        minus = ctk.CTkButton(gui2, text=' - ')
        minus.configure(command=functools.partial(operand_press_switch, '-'))
        minus.grid(row=brn + 4, column=3)

        multiply = ctk.CTkButton(gui2, text=' * ')
        multiply.configure(command=functools.partial(operand_press_switch, '*'))
        multiply.grid(row=brn + 5, column=3)

        divide = ctk.CTkButton(gui2, text=' / ')
        divide.configure(command=functools.partial(operand_press_switch, '/'))
        divide.grid(row=brn + 6, column=3)

        equal = ctk.CTkButton(gui2, text=' = ', command=equalpress)
        equal.grid(row=brn + 6, column=2, padx=10, pady=10)

        clear = ctk.CTkButton(gui2, text='Clear', command=clear)
        clear.grid(row=brn + 5, column='0', padx=10, pady=10)

        undo_button = ctk.CTkButton(gui2, text='Undo', font=('arial', 20, 'bold'))
        undo_button.configure(command=remember())
        undo_button.grid(row=brn + 6, column=0)

        Lbracket = ctk.CTkButton(gui2, text='(', command=lambda: press('('))
        Lbracket.grid(row=brn + 5, column=1)

        Rbracket = ctk.CTkButton(gui2, text=')', command=lambda: press(')'))
        Rbracket.grid(row=brn + 5, column=2)

        timer_string_var = ctk.StringVar(gui2)
        time_b = ctk.CTkButton(gui2, textvariable=timer_string_var)
        time_b.configure(state="disabled", fg_color='red', text_color_disabled='white')
        time_b.grid(row=brn + 1, column=1)

        t_seconds = 3

        def update_gui2():
            global t_seconds
            timer = datetime.timedelta(seconds=t_seconds)
            timer_string_var.set(timer)
            t_seconds -= 1
            if (t_seconds == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
            gui2.update()
            gui2.after(1000, update_gui2)

        gui2.after(1000, update_gui2)

        solutions_list()
        gui2.mainloop()  # start the gui2

    def run_letters_game(self):
        number_of_vowels = ctk.CTkInputDialog(text = "How many Vowels? [3,4,5]", title = 'Vowels')
        nov = number_of_vowels.get_input()
        nov = int(nov)
        if nov < 3 or nov > 5:
            self.run_letters_game()
        gui = ctk.CTkToplevel(self)
        gui.geometry('1000x200')
        gui.configure(background="black")  # set the background colour of GUI window
        gui.title("Countdown Letters")  # set the title of GUI window

        def making_letters():
            # First, let's define a list of letters
            consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'W',
                          'Y','Z']
            vowels = ['A', 'E', 'I', 'O', 'U']
            vow = random.choices(vowels, weights=(15, 21, 13, 13, 5), k=nov)
            number_of_consonants = 9 - nov
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
            best_words_text = ctk.CTkTextbox(gui, height = 40)
            best_words_text.grid(row=3, column=2, padx=20, pady=(20, 10))
            best_words_text.insert('0.0', f'{longest_words}' )

        def display_all_words():
            all_words_text = ctk.CTkTextbox(gui, height = 40)
            all_words_text.grid(row=3, column=4, padx=20, pady=(20, 10))
            all_words_text.insert('0.0', f'{all_possible}' )


        making_letters()
        bcn = 0  # Base column number

        letter0 = ctk.CTkButton(gui, text=f' {letters[0]} ', font=('arial', 20, 'bold'))
        letter0.configure(state="disabled")
        letter0.grid(row=1, column=bcn, padx = 20, pady = 5)

        letter1 = ctk.CTkButton(gui, text=f' {letters[1]} ', font=('arial', 20, 'bold'))
        letter1.configure(state="disabled")
        letter1.grid(row=1, column=bcn + 1, padx = 20, pady = 5)

        letter2 = ctk.CTkButton(gui, text=f' {letters[2]} ', font=('arial', 20, 'bold'))
        letter2.configure(state="disabled")
        letter2.grid(row=1, column=bcn + 3, padx = 20, pady = 5)

        letter3 = ctk.CTkButton(gui, text=f' {letters[3]} ', font=('arial', 20, 'bold'))
        letter3.configure(state="disabled")
        letter3.grid(row=1, column=bcn + 4, padx = 20, pady = 5)

        letter4 = ctk.CTkButton(gui, text=f' {letters[4]} ', font=('arial', 20, 'bold'))
        letter4.configure(state="disabled")
        letter4.grid(row=2, column=bcn + 0, padx = 20, pady = 5)

        letter5 = ctk.CTkButton(gui, text=f' {letters[5]} ', font=('arial', 20, 'bold'))
        letter5.configure(state="disabled")
        letter5.grid(row=2, column=bcn + 1, padx = 20, pady = 5)

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

        entry = ctk.CTkEntry(gui, width = 200)
        entry.grid(row=0, column=2)

        best_words = ctk.CTkButton(gui, text = 'Display best words', command = display_best_words)
        best_words.grid(row = 3, column = 1)

        all_words = ctk.CTkButton(gui, text='Display all words', command=display_all_words)
        all_words.grid(row=3, column=3)

        score_label = ctk.CTkLabel(gui, text = f'Score: {score}')
        score_label.grid(row = 0, column = 0)



        buttonc = Button(gui, text=f'Constant button')

        # vowels_label = ctk.CTkLabel(gui, text="vowels:", anchor="w")
        # vowels_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        # vowels_optionmenu = ctk.CTkOptionMenu(gui, values=['3', '4', '5'])
        # vowels_optionmenu.grid(row=6, column=0)

        # timer_string_var = ctk.StringVar(gui)
        # time_b = ctk.CTkButton(gui, textvariable=timer_string_var)
        # time_b.configure(state="disabled", fg_color='red', text_color_disabled='white')
        # time_b.grid(row= 3 , column=1)
        # time_left = 60
        # def update_label(time_left):
        #     if time_left > 0:
        #         time_left -= 1
        #         ctk.CTkLabel.config(text=str(time_left))
        #         ctk.CTkLabel.after(1000, update_label)
        #     else:
        #         ctk.CTkLabel.config(text="Time's up!")
        #
        #   # change this to set the starting time
        # label = ctk.CTkLabel(gui, text=str(time_left))
        # label.grid(row = 3, column = 0)
        # update_label(time_left)

        # t_seconds = 30
        #
        # def update_gui():
        #     global t_seconds
        #     timer = datetime.timedelta(seconds=t_seconds)
        #     timer_string_var.set(timer)
        #     t_seconds -= 1
        #     if (t_seconds == 0):
        #         messagebox.showinfo("Time Countdown", "Time's up ")
        #     gui.update()
        #     gui.after(1000, update_gui)
        #
        # gui.after(1000, update_gui)

        gui.mainloop()

    # def close(self):
    #     save_score = input('Would you like to save your score? [Yes, No]')
    #     if save_score == 'Yes':
    #         pass
    #         #file.write(score)

if __name__ == "__main__":
    app = App()
    app.mainloop()