# imports
import datetime
from tkinter import messagebox

import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry(f"{1100}x{580}")
        self.title("Countdown")
        self.resizable(True, True)
        self.sidebar_frame = Sidebar(self)

        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent_app):
        super().__init__(parent_app, width=140, corner_radius=0)
        self.change_scaling_event = None
        self.change_appearance_mode_event = None
        self.run_letters_game = None
        self.sidebar_button_event = None
        self.parent_app = parent_app
        # create sidebar frame with widgets
        self.logo_label = ctk.CTkLabel(self, text="Countdown",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self, text='Home', command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.play_numbers_game = ctk.CTkButton(self, text='Numbers Game', command=self.make_f1)
        self.play_numbers_game.grid(row=2, column=0, padx=20, pady=10)
        # self.play_letters_game = ctk.CTkButton(self, text='Letters Game', command=self.run_letters_game)
        # self.play_letters_game.grid(row=3, column=0, padx=20, pady=10)
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

    def make_f1(self):
        Frame = Frame1()
        Frame.mainloop()


# class Tabview(ctk.CTkFrame):
#     # create tabview
#     def __init__(self, parent_app):
#         super.__init__(parent_app)
#         self.tabview = ctk.CTkTabview(self, width=250)
#         self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
#         self.tabview.add("Information about the Game")
#         self.tabview.add("How to Play")
#         self.tabview.add("About the Developer")
#         self.tabview.tab("Information about the Game").grid_columnconfigure(0,
#                                                                             weight=1)  # configure grid of individual tabs
#         self.tabview.tab("How to Play").grid_columnconfigure(0, weight=1)
#         self.tabview.tab("About the Developer").grid_columnconfigure(0, weight=1)
#
#         # create textbox
#         self.textbox_info = ctk.CTkTextbox(self.tabview.tab("Information about the Game"), width=900)
#         self.textbox_info.grid(row=0, column=0, padx=20, pady=(20, 10))
#         self.textbox_info.insert('0.0', """
#         Countdown is a popular television show game which has been aired since 1982.
#         The game has three sections: Letters, Numbers and Conundrum.
#
#         The letters version provides 9 letters of which the player can choose either 3,4 or 5 vowels
#         and the remaining letters to be consonants.
#         From these 9 characters, the aim is to make the longest word possible within the time frame.
#
#         The numbers version is similar, the user is prompted to pick the amount of 'big numbers',
#         with a maximum of 4 and the remaining numbers are 'small numbers'.
#         Provided with these numbers, a target number is provided and the user's aim is to reach this
#         target number or as close to as possible within the time frame.
#
#         Conundrum, is the final version where a 9 letter anagram is provided and the aim is to find
#         the 9 letter word from this.
#         """)
#
#         self.textbox_htp = ctk.CTkTextbox(self.tabview.tab("How to Play"), width=250)
#         self.textbox_htp.grid(row=0, column=0, padx=20, pady=(20, 10))
#         self.textbox_htp.insert('0.0', 'Hi there')
#
#         self.textbox_atd = ctk.CTkTextbox(self.tabview.tab("About the Developer"), width=250)
#         self.textbox_atd.grid(row=0, column=0, padx=20, pady=(20, 10))
#         self.textbox_atd.insert('0.0', 'Hi there')
#
#         self.login = ctk.CTkButton(self, text="Log in", command=self.log_in)
#         self.login.grid(row=0, column=2, padx=20, pady=20)
#
#         # self.close = ctk.CTkButton(self, text = 'Close', command = self.close)
#         self.login.grid(row=2, column=2, padx=20, pady=20)
#         # self.appearance_mode_optionemenu.set("Dark")
#         # self.scaling_optionemenu.set("100%")
class timer(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.timelabel = ctk.CTkLabel(self, text=f'Score: {self.timer}')
        self.timelabel.grid(row=0, column=1)

        self.t_seconds = 30
        def update_gui():
            timer = datetime.timedelta(seconds=self.t_seconds)
            timer_string_var.set(timer)
            self.t_seconds -= 1
            if (self.t_seconds == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
            self.update()
            self.after(1000, update_gui)

        self.after(1000, update_gui)

class Frame1(ctk.CTkToplevel):
    def __init__(self, parent_app):
        super().__init__(parent_app)
        self.SidebarFrame = Sidebar(self)
        self.SidebarFrame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.SidebarFrame.grid_rowconfigure(4, weight=1)
        self.title('Fram1')


if __name__ == "__main__":
    app = App()
    app.mainloop()
