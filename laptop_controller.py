from laptop_csv_reader import CSVdata
from laptopUI import LaptopUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class LaptopController:

    def __init__(self, csv_data):
        self.data = csv_data
        self.model = LaptopUI(self.data)

    def start(self):
        self.model.start()

    def data(self):
        return self.data
