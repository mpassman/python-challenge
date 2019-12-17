import csv

def readMyFile(election_data):
    dates = []
    scores = []

    with open(election_data.csv) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            dates.append(row[0])
            scores.append(row[1])

    return dates, scores


dates,scores = readMyFile('file.csv')

print(dates)
print(scores)