#Import Resources

import os
import csv

print("Election Results")
print("-----------------------")

#Count Total Votes
#Set File Path
election_csv_path = os.path.join("Resources", "election_data.csv")
##print (budget_csv_path)
with open(election_csv_path) as csvfile:
    electioncsvreader = csv.reader(csvfile, delimiter=",")
    #Skip first line
    next(electioncsvreader)
    totalvotes = 0
    #Search through each row
    for row in electioncsvreader:
        #add profit amount to total
        totalvotes = (totalvotes+1)
         

print(f"Total Votes: {totalvotes}")
print("-----------------------")

#list of Candidates

candidates = []

#add candidates to list
#Set File Path
election_csv_path = os.path.join("Resources", "election_data.csv")
##print (budget_csv_path)
with open(election_csv_path) as csvfile:
    electioncsvreader = csv.reader(csvfile, delimiter=",")
    #Skip first line
    next(electioncsvreader)
    #Search through each row
    for row in electioncsvreader:
        #if Candidate is not on list
        if (row[2]) not in (candidates):
            #append candidates to list
            candidates.append(row[2])

#print(candidates)


