import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from laptop_csv_reader import CSVdata
from menu import Menu


class LaptopUI(ctk.CTk):

    def __init__(self):
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

    def main_menu(self):
        self.menu = Menu(self)

    def start(self):
        self.mainloop()


LaptopUI()
