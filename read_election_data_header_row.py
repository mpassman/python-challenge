import csv
import pprint

with open("election_data.csv", "r") as f:
    csv_reader = csv.reader(f)
    header = next(csv_reader)
    data = list(csv_reader)
    row_count = len(data)
    def candidate(vote,dic):
        for candidate in dic.items():

            [candidate] = dic[candidate] + 1
    candidates = list()

print ("Total Votes: ")
print (row_count)
print (candidate)