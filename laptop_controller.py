from laptopUI import LaptopUI, COMPARE_DATA
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class LaptopController:

    def __init__(self, csv_data):
        self.data = csv_data
        self.model = LaptopUI(self.data)
        self.master = self.model.master
        self.selected_index = None
        self.compare_data = COMPARE_DATA

    def start(self):
        self.model.start()

    def data(self):
        return self.data

    def receive_selected_index(self, selected_index):
        self.selected_index = selected_index
