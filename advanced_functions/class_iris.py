import csv

class Iris:
    def __init__(self,filename):
        raw_data = self.load_data(filename)
        self.header = raw_data[0]
        self.data = raw_data[1:]

    def load_data(self, filename):
        with open(filename) as open_file:
            csv_reader = csv.reader(open_file)
            return list(csv_reader)


iris = Iris("iris.csv")
print(iris.header)
