"""This module is to run the program"""
from laptop_controller import LaptopController
from laptop_csv_reader import CSVdata


def main():
    csv_file = CSVdata('laptop_price.csv')
    csv_data = csv_file.read_csv()
    data = csv_file.get_data()
    app = LaptopController(data)
    app.start()


if __name__ == '__main__':
    main()
