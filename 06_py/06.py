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

print(reader)

workforce_dict = {}

for row in reader:
    print(row)
    workforce_dict[row['Job Class']] = row['Percentage']

print(workforce_dict)
