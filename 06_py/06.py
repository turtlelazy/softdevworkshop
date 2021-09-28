"""
Ishraq Mahid
Softdev
k06 -- Weighted Probability
2021-9-28
"""

import csv

csv_file = open("occupations.csv")

"""
spamreader = csv.reader(csv_file, delimiter=' ', quotechar='|')
for row in spamreader:
    print(', '.join(row))

"""
reader = csv.DictReader(csv_file)

#print(reader)

workforce_dict = {}
tickets = []

for row in reader:
    #print(row)
    workforce_dict[row['Job Class']] = row['Percentage']
    percentage = int(float(row['Percentage'])*10)
    #print(percentage)
    for i in range(percentage):
        if(row['Job Class'] != 'Total'):
            tickets.append(row['Job Class'])

#print(workforce_dict)
print(tickets)
