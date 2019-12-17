import csv

with open("election_data.csv", "r") as f:
    csv_reader = csv.reader(f)

    header = next(csv_reader)

    data = list(csv_reader)
    # print(data)

    for e in data:
            print(e)




    