import customtkinter as ctk
from laptopUI import *


class LaptopController(ctk.CTk):
    def __init__(self, csv_data):
        super().__init__()
        self.data = csv_data
        self.compare_data = []

        # set up
        ctk.set_appearance_mode('dark')
        self.geometry('1000x500')
        self.minsize(900, 500)

        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        self.menu = Menu(self, data=self.data)
        self.menu.grid(row=0, column=0)

    def start(self):
        self.mainloop()

    def master(self):
        return self.master

    def receive_compare_data(self, compare_data):
        print(compare_data)
        self.compare_data = compare_data
