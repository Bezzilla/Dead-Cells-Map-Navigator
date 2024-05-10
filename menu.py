import customtkinter as ctk


class Menu(ctk.CTkTabview):

    def __init__(self, parent):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew')

        # taps
        self.add('Data comparison')
        self.add('Story telling')

        Data_Comparison(self.tab('Data comparison'))
        Story_Telling(self.tab('Story telling'))


class Data_Comparison(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')
        Search_Panel(self, text="Search Box")


class Story_Telling(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')


class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='#4a4a4a')
        self.pack(fill='x', pady=4, padx=4)


class Search_Panel(Panel):

    def __init__(self, parent, text):
        super().__init__(parent=parent)

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(self, text=text).grid(row=0, column=0
                                           , sticky='w', padx=5, pady=5)

        ctk.CTkEntry(self).grid(row=1, column=0, sticky='w', padx=5, pady=5)

        ctk.CTkButton(self,text="Search").grid(row=1,column=1, sticky='E'
                                               , padx=5, pady=5)
