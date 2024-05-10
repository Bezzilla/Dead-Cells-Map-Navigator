import customtkinter as ctk
from menu import Menu


class LaptopUI(ctk.CTk):

    def __init__(self,csv_data):
        super().__init__()
        # set up

        ctk.set_appearance_mode('dark')
        self.geometry('1000x500')
        self.minsize(900, 500)

        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')
        self.main_menu()

        # data
        self.data = csv_data

    def main_menu(self):
        Menu(self)

    def start(self):
        self.mainloop()
