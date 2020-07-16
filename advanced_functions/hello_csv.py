import csv

# READ
# scores = []
with open("some_data.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    headers = list(map(str.lstrip,next(csvreader)))
    # for row in csvreader:
    #     scores.append(int(row[-1]))

print(headers)
#print(scores)

# WRITE
# data_to_write = [["David",5],["Juxhen",6],["Mason",17]]
# with open("new_data.csv", "w") as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerows(data_to_write)


