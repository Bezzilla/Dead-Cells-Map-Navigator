from laptopUI import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import customtkinter as ctk


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

        self.graph_frame = ctk.CTkFrame(self)
        self.graph_frame.grid(row=0, column=1, sticky="nsew")

    def start(self):
        self.mainloop()

    def master(self):
        return self.master

    def receive_compare_data(self, compare_data):
        for i in compare_data:
            self.compare_data += [self.data[int(i)]]
        self.create_compare_graph()

    def create_compare_graph(self):
        # Extracting prices and index [1] from the compared data
        prices = [float(item[-2]) for item in self.compare_data]
        product = [item[1] for item in self.compare_data]

        # Plotting the graph
        fig, ax = plt.subplots()
        ax.plot(product, prices, marker='o', linestyle='-')
        ax.set_xlabel('Product')
        ax.set_ylabel('Price')
        ax.set_title('Price vs Product')
        ax.grid(True)

        # Embedding the plot into the tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both',
                                    expand=True, padx=20, pady=20)

    def plot_box_price(self):
        pass

    def plot_histogram(self):
        # Extracting prices from the data, skipping invalid entries
        prices = [float(item[-2]) for item in self.data if item[-2].isdigit()]

        # Plotting the histogram
        fig = plt.figure(figsize=(8, 6))
        sns.histplot(prices, bins=20, kde=True)
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.title('Distribution of Laptop Prices')
        plt.grid(True)

        # Embedding the plot into a new frame

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, padx=20, pady=20)

    def plot_scatter(self):
        pass
