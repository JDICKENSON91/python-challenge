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

#get totals for each candidate

totalfirst = 0
totalsecond = 0
totalthird = 0
totalfourth = 0

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
        if (row[2]) == (candidates[0]):
            #append candidates to list
            totalfirst = (totalfirst +1)
        if (row[2]) == (candidates[1]):
            #append candidates to list
            totalsecond = (totalsecond +1)
        if (row[2]) == (candidates[2]):
            #append candidates to list
            totalthird = (totalthird +1)
        if (row[2]) == (candidates[3]):
            #append candidates to list
            totalfourth = (totalfourth +1)

firstpercent = (int(totalfirst/totalvotes*100))
secondpercent = (int(totalsecond/totalvotes*100))
thirdpercent = (int(totalthird/totalvotes*100))
fourthpercent = (int(totalfourth/totalvotes*100))


print(f"{candidates[0]}: {firstpercent}% ({totalfirst})")
print(f"{candidates[1]}: {secondpercent}% ({totalsecond})")
print(f"{candidates[2]}: {thirdpercent}% ({totalthird})")
print(f"{candidates[3]}: {fourthpercent}% ({totalfourth})")

print("-----------------------")

listoftotals = [totalfirst,totalsecond,totalthird,totalfourth]
winner = ""

#print(listoftotals)

if max(listoftotals) == totalfirst:
    winner = candidates[0]
if max(listoftotals) == totalsecond:
    winner = candidates[1]
if max(listoftotals) == totalthird:
    winner = candidates[2]
if max(listoftotals) == totalfourth:
    winner = candidates[3]

print(f"Winner: {winner}")
print("-----------------------")   

#output file

#Specify the file to write to
output_path = os.path.join("analysis", "Election_Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline="") as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerow([f"Total Votes: {totalvotes}"])
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerow([f"{candidates[0]}: {firstpercent}% ({totalfirst})"])
    csvwriter.writerow([f"{candidates[1]}: {secondpercent}% ({totalsecond})"])
    csvwriter.writerow([f"{candidates[2]}: {thirdpercent}% ({totalthird})"])
    csvwriter.writerow([f"{candidates[3]}: {fourthpercent}% ({totalfourth})"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-----------------------"])   


