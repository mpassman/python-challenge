import csv
import pprint

with open("election_data.csv", "r") as f:
    csv_reader = csv.reader(f)
    headers = next(csv_reader)
    data = list(csv_reader)
    
datalist = []
for row in datareader:
        data = {}
        for i in range (4):
            data[headers[i]] = row[i]
        datalist.append(data)

for data in datalist: 
    
    print[data]
   
print ("Total Votes: ")
print (row_count)
