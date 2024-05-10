from laptop_controller import LaptopController
from laptop_csv_reader import CSVdata
if __name__ == '__main__':
    csv_file = CSVdata('laptop_price.csv')
    csv_data = csv_file.read_csv()
    data = csv_file.get_data()
    # for i in data1:
    #     print(i)
    app = LaptopController(data)
    app.start()
