from laptop_csv_reader import CSVdata
from laptopUI import LaptopUI


class LaptopController:

    def __init__(self,csv_data):
        self.data = csv_data
        self.model = LaptopUI(self.data)

    def start(self):
        self.model.start()
