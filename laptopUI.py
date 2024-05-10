import customtkinter as ctk
from CTkListbox import *


class LaptopUI(ctk.CTk):

    def __init__(self, csv_data):
        super().__init__()
        # set up

        ctk.set_appearance_mode('dark')
        self.geometry('1000x500')
        self.minsize(900, 500)

        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        Menu(self).grid(row=0, column=0)
        print(1)

        # self.graph = ctk.CTkLabel(self,text="test",fg_color="red")
        # self.graph.grid(row=0,column=1,sticky="NSEW",padx=20,pady=20)
        # data
        self.data = csv_data

    def start(self):
        self.mainloop()


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
        # Comparison_Panel(self, text="Result")
        Selected_Panel(self, text="Selected")


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

        self.rowconfigure((0, 1, 2, 3), weight=1)
        self.columnconfigure(0, weight=1)

        self.search_label = ctk.CTkLabel(self, text=text)
        self.search_label.grid(row=0, column=0, sticky='N', padx=5, pady=5)

        self.search_panel = ctk.CTkEntry(self)
        self.search_panel.grid(row=1, column=0, sticky='EW', padx=5, pady=5)
        self.search_panel.bind("<KeyRelease>", self.on_key_release)

        self.compare_list_box = CTkListbox(self, width=250)
        self.compare_list_box.grid(row=2, column=0, sticky='EW', padx=5,
                                   pady=5)

        self.add_button = ctk.CTkButton(self, text="Add to Compare List")
        self.add_button.grid(row=3, column=0, sticky='EW', padx=5, pady=5)

    def on_key_release(self, event):
        search_text = self.search_panel.get()
        print(search_text)


class Comparison_Panel(Panel):

    def __init__(self, parent, text):
        super().__init__(parent=parent)

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)

        self.compare_label = ctk.CTkLabel(self, text=text)
        self.compare_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        self.compare_list_box = CTkListbox(self, width=250)
        self.compare_list_box.grid(row=1, column=0, sticky='EW', padx=5,
                                   pady=5)


class Selected_Panel(Panel):
    def __init__(self, parent, text):
        super().__init__(parent=parent)

        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)

        self.selected_label = ctk.CTkLabel(self, text=text)
        self.selected_label.grid(row=0, column=0, sticky='N', padx=5, pady=5,
                                 columnspan=3)

        self.compare_list_box = CTkListbox(self, width=250)
        self.compare_list_box.grid(row=1, column=0, sticky='EW', padx=5,
                                   pady=5, columnspan=3)

        self.del_button = ctk.CTkButton(self, text="Delete")
        self.del_button.grid(row=2, column=0, sticky='N', padx=5,
                             pady=5)

        self.compare_button = ctk.CTkButton(self, text="Compare")
        self.compare_button.grid(row=2, column=1, padx=5,
                                 pady=5)

        self.clear_button = ctk.CTkButton(self, text="Clear")
        self.clear_button.grid(row=2, column=2, padx=5,
                               pady=5)
