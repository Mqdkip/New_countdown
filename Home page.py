import tkinter
import tkinter.messagebox
import customtkinter
import csv

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
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
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Countdown", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text = 'Home', command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text = 'Numbers Game', command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text = 'Letters Game', command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button


        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Information about the Game")
        self.tabview.add("How to Play")
        self.tabview.add("About the Developer")
        self.tabview.tab("Information about the Game").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("How to Play").grid_columnconfigure(0, weight=1)
        self.tabview.tab("About the Developer").grid_columnconfigure(0, weight=1)

        # create textbox
        self.textbox_info = customtkinter.CTkTextbox(self.tabview.tab("Information about the Game"), width=900)
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

        self.textbox_htp = customtkinter.CTkTextbox(self.tabview.tab("How to Play"), width=250)
        self.textbox_htp.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.textbox_htp.insert('0.0', 'Hi there')

        self.textbox_atd = customtkinter.CTkTextbox(self.tabview.tab("About the Developer"), width=250)
        self.textbox_atd.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.textbox_atd.insert('0.0', 'Hi there')

        self.login = customtkinter.CTkButton(self, text="Log in", command=self.log_in)
        self.login.grid(row = 0, column = 2, padx = 20, pady = 20)

        self.close = customtkinter.CTkButton(self, text = 'Close', command = self.close)
        self.login.grid(row=2, column=2, padx=20, pady=20)

        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
        #                                                    command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)







        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        #self.optionmenu_1.set("CTkOptionmenu")
        #self.combobox_1.set("CTkComboBox")

        #self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)


    def log_in(self):
        Password = customtkinter.CTkInputDialog(text="Password:", title="Log in")
        Username = customtkinter.CTkInputDialog(text="Username:", title="Log in")
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
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def close(self):
        save_score = input('Would you like to save your score? [Yes, No]')
        if save_score == 'Yes':
            pass
            #file.write(score)








if __name__ == "__main__":
    app = App()
    app.mainloop()