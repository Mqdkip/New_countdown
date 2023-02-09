# imports
import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
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


class Frame1(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.SidebarFrame = Sidebar(self)
        self.SidebarFrame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.SidebarFrame.grid_rowconfigure(4, weight=1)
        self.title('Fram1')


if __name__ == "__main__":
    app = App()
    app.mainloop()
