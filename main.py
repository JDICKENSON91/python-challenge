#Import Resources

import os
import csv

print("Financial Analysis")

#set variable for months (ignore header row)
totalmonths = -1

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
        
print("----------------------------------------")   
print(f"Total Months: {totalmonths}")


#Set File Path
budget_csv_path = os.path.join("Resources", "budget_data.csv")
##print (budget_csv_path)
with open(budget_csv_path) as csvfile:
    budgetcsvreader = csv.reader(csvfile, delimiter=",")
    #Skip first line
    next(budgetcsvreader)
    pltotal = 0.00
    #Search through each row
    for row in budgetcsvreader:
        #add profit amount to total
        pltotal = (float(row[1]) + pltotal)
         
print(f"Total: ${pltotal}")

#Find Last Value

#Set File Path
budget_csv_path = os.path.join("Resources", "budget_data.csv")
LASTvalue = 0.00
##print (budget_csv_path)
with open(budget_csv_path) as csvfile:
    budgetcsvreader = csv.reader(csvfile, delimiter=",")
    #Skip first line
    next(budgetcsvreader)
    #Search through each row
    for row in budgetcsvreader:
        #Find Last Value
        LASTvalue = (float(row[1]))

#Find First Value

#Set File Path
budget_csv_path = os.path.join("Resources", "budget_data.csv")
FIRSTvalue = 0.00
SS = 0
##print (budget_csv_path)
with open(budget_csv_path) as csvfile:
    budgetcsvreader = csv.reader(csvfile, delimiter=",")
    #Skip first line
    next(budgetcsvreader)
    #Search through each row
    for row in budgetcsvreader:
        SS == 0
        #Find Last Value
        FIRSTvalue = (float(row[1]))
        if SS == 0:
            break
    
#print(FIRSTvalue)
#print(LASTvalue)

avdifftotal = (LASTvalue - FIRSTvalue) /(totalmonths  - 1)
print(f"Total: ${avdifftotal}")

#Set File Path
budget_csv_path = os.path.join("Resources", "budget_data.csv")
##print (budget_csv_path)

# Set List

#Scan through list, log prev value, current value and difference. If difference is bigger then last difference  overide current and prev with new values.


Maxvalue = 0.00
Dateofmax = ""
MaxPH = 0.00
lastvalue = 0.00
currentvalue = 0.00
maxchange = 0.00

with open(budget_csv_path) as csvfile:
    budgetcsvreader = csv.reader(csvfile, delimiter=",")
    #Skip first line
    next(budgetcsvreader)
    #Search through each row
    for row in budgetcsvreader:
        #see if value is higher than previous value
        lastvalue = currentvalue
        currentvalue = (float(row[1]))
        MaxPH = currentvalue - lastvalue
        if (Maxvalue < MaxPH):
            Dateofmax = (row[0])
            Maxvalue = MaxPH
            lastvalue = (float(row[1]))

print(f"Greatest Increase in Profits: {Dateofmax} (${Maxvalue})")

#Set File Path
budget_csv_path = os.path.join("Resources", "budget_data.csv")
##print (budget_csv_path)

# Set List

#Scan through list, log prev value, current value and difference. If difference is bigger then last difference  overide current and prev with new values.


Minvalue = 0.00
Dateofmin = ""
MinPH = 0.00
lastvalue = 0.00
currentvalue = 0.00
minchange = 0.00

with open(budget_csv_path) as csvfile:
    budgetcsvreader = csv.reader(csvfile, delimiter=",")
    #Skip first line
    next(budgetcsvreader)
    #Search through each row
    for row in budgetcsvreader:
        #see if value is higher than previous value
        lastvalue = currentvalue
        currentvalue = (float(row[1]))
        MinPH = currentvalue - lastvalue
        if (Minvalue > MinPH):
            Dateofmin = (row[0])
            Minvalue = MinPH
            lastvalue = (float(row[1]))

print(f"Greatest Decrease in Profits: {Dateofmin} (${Minvalue})")



