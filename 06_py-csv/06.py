"""
Ishraq Mahid, Gavin McGinley, Ivan Mijacika - Cool Dogs
Softdev
k06 -- Weighted Probability
2021-9-28
"""

"""
#SUMMARY OF TRIO DISCUSSION 
We mainly focused on ideas for weighting based on percentages. We had roughly the
same ideas on how to parse the csv file (following documentation), but the algorithm
that would process that data was much more confusing. Eventually, we thought of approaching
the issue with a list, appending the job category for each 0.1 percent, and then choosing
randomly from the list. This would weight the jobs

#DISCOVERIES
We looked at the csv module documentation and figured out how to use it.

#QUESTIONS 
What is the better way to do weighted averages? Our group felt that utilizing a list in 
this manner had to be vastly inferior and ineffecient compared to the best solution,
despite not knowing what the best solution is.

#COMMENTS
This method also limits scalability. If sig figs increase, some code has to be created
in response.
"""
import csv, random

###Reading .csv file
csv_file = open("occupations.csv")

reader = csv.DictReader(csv_file)

#print(reader)

###Taking data from csv and placing into db
workforce_dict = {}
tickets = []

for row in reader:
    #print(row)
    workforce_dict[row['Job Class']] = float(row['Percentage'])
    percentage = int(float(row['Percentage'])*10)
    #print(percentage)
    for i in range(percentage):
        if(row['Job Class'] != 'Total'):
            tickets.append(row['Job Class'])

###Gets randomJob, weighted
def randomJob(list):
    return random.choice(list)

print(randomJob(tickets))
