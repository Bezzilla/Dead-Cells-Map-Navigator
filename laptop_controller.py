"""This module is to control laptopUI"""

from laptopUI import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import pandas as pd
import customtkinter as ctk


class LaptopController(ctk.CTk):
    """main control"""
    def __init__(self, csv_data):
        """initiated component"""
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

        self.graph_frame = ctk.CTkFrame(self)
        self.graph_frame.grid(row=0, column=1, sticky="nsew")

    def start(self):
        self.mainloop()

    def master(self):
        return self.master

    def receive_compare_data(self, compare_data):
        """receive data from button"""
        for i in compare_data:
            self.compare_data += [self.data[int(i)]]
        self.create_compare_graph()

    def create_compare_graph(self):
        """create compare graph"""
        prices = [float(item[-2]) for item in self.compare_data]
        product = [item[1] for item in self.compare_data]

        fig, ax = plt.subplots()
        ax.plot(product, prices, marker='o', linestyle='-')
        ax.set_xlabel('Product')
        ax.set_ylabel('Price')
        ax.set_title('Price vs Product')
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both',
                                    expand=True, padx=20, pady=20)

    def plot_box_price(self):
        """create box plot"""
        prices = [float(item[-1]) for item in self.data if
                  item[-1].replace('.', '').isdigit()]

        fig = plt.figure(figsize=(8, 6))
        sns.boxplot(y=prices, color='skyblue')
        plt.ylabel('Price')
        plt.title('Distribution of Laptop Prices')
        plt.grid(True)

        self.plot_graph(fig)

    def plot_histogram(self):
        """create histogram"""
        prices = [float(item[-2]) for item in self.data if item[-2].isdigit()]

        fig = plt.figure(figsize=(8, 6))
        sns.histplot(prices, bins=20, kde=True)
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.title('Distribution of Laptop Prices')
        plt.grid(True)

        self.plot_graph(fig)

    def plot_scatter(self):
        """create scatter plot"""
        screen_sizes = [float(item[3]) for item in self.data if
                        item[3].replace('.', '').isdigit()]
        prices = [float(item[-1]) for item in self.data if
                  item[-1].replace('.', '').isdigit()]

        fig = plt.figure(figsize=(8, 6))
        plt.scatter(screen_sizes, prices, alpha=0.5)
        plt.xlabel('Screen Size (inches)')
        plt.ylabel('Price')
        plt.title('Price vs Screen Size')
        plt.grid(True)

        self.plot_graph(fig)

    def show_descriptive_statistics(self):
        """show descriptive statistic"""
        numerical_data = [
            [float(val) if val.replace('.', '').isdigit() else None for val in
             item[3:]] for item in self.data]

        df = pd.DataFrame(numerical_data,
                          columns=['inches', 'screenresolution', 'cpu', 'ram',
                                   'memory', 'gpu', 'opsys', 'weight', 'price',
                                   'index'])

        statistics = df.describe()

        statistics_str = statistics.to_string()

        descriptive = ctk.CTkLabel(self, text=statistics_str,
                                   font=("Helvetica", 20))
        descriptive.grid(row=0, column=1, padx=20, pady=20, stick="NSEW")

    def plot_graph(self, fig):
        """plot graph in custom tkinter"""
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, padx=20, pady=20)
