import csv


class CSVdata:
    def __init__(self, file_path):
        self.data = []
        self.file_path = file_path

    def read_csv(self):
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            self.data = list(reader)
            for i in range(len(self.data)):
                self.data[i] += [str(i)]

    def get_data(self):
        return self.data
