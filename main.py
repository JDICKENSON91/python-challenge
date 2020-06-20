#Import Resources

import os
import csv

#Set Variables
totalmonths = -1
totalprofitloss = 0


#Set File Path
budget_csv_path = os.path.join("Resources", "budget_data.csv")
##print (budget_csv_path)

# Open the CSV
with open(budget_csv_path) as csvfile:
    budgetcsvreader = csv.reader(csvfile, delimiter=",")
    #Search through each row
    for row in budgetcsvreader:
        #Accumulate the months
        totalmonths = int(totalmonths+1)
    for row in budgetcsvreader:
        print ("a")
        #Accumulate the total
        #pl = row[1]
        #totalprofitloss = float(totalprofitloss + pl)

print (totalmonths)
print (totalprofitloss)
        


#The total number of months included in the dataset


#The net total amount of "Profit/Losses" over the entire period


#The average of the changes in "Profit/Losses" over the entire period


#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period