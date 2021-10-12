import csv, random

jobPercentages = {}
totalPercentage = 100

def init():             # Reading CSV file
    global totalPercentage
    with open('data\occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row["Job Class"]
            percentage = float(row["Percentage"])
            if job == 'Total':
                totalPercentage = percentage
            else:
                jobPercentages[job] = float(percentage)
    return jobPercentages

def chooseRandom():     # Choosing random value based on weighted percentages. 
    randVal = random.uniform(0, totalPercentage)
    for k, v in jobPercentages.items():
        randVal -= v
        if randVal <= 0:
            return k