import csv
# Write a function that will read in the iris dataset
# Write a function that will return the mean for each 'column'
# Write a function that will write the means to a new csv file

def iris_reader(cvsfile):
    with open("iris.csv","r") as csvfile:
        csvreader = csv.reader(csvfile)
        print(list(csvfile))


def get_mean(cvsfile, cvsreader):
    with open("iris.csv", "r") as csvfile:
        csvreader = list(csv.reader(csvfile))
        csvreader = csvreader[1:]
        mean_of_columns = []
        for i in range(4):
            sum = 0
            for row in csvreader:
                sum += float(row[i])
            mean = sum / (len(list(csvreader)))
            mean_of_columns.append(mean)
        return mean_of_columns


mean = get_mean("iris.csv", iris_reader("iris.csv"))

result = [["sepal_length_mean", mean[0]], ["sepal_width_mean", mean[1]], ["petal_length_mean", mean[2]], ["petal_width_mean", mean[3]]]

with open("mean_iris.csv","w") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(result)

