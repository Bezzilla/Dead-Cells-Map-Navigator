from laptop_csv_reader import CSVdata
from laptopUI import LaptopUI


class LaptopController:

    def __init__(self):
        self.model = LaptopUI()

    def start(self):
        self.model.start()
