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
    pltotal = 0
    #Search through each row
    for row in budgetcsvreader:
        #add profit amount to total
        pltotal = (int(row[1]) + pltotal)
         
print(f"Total: ${pltotal}")

#Find Last Value

#Set File Path
budget_csv_path = os.path.join("Resources", "budget_data.csv")
LASTvalue = 0
##print (budget_csv_path)
with open(budget_csv_path) as csvfile:
    budgetcsvreader = csv.reader(csvfile, delimiter=",")
    #Skip first line
    next(budgetcsvreader)
    #Search through each row
    for row in budgetcsvreader:
        #Find Last Value
        LASTvalue = (int(row[1]))

#Find First Value

#Set File Path
budget_csv_path = os.path.join("Resources", "budget_data.csv")
FIRSTvalue = 0
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
        FIRSTvalue = (int(row[1]))
        if SS == 0:
            break
    
#print(FIRSTvalue)
#print(LASTvalue)

avdifftotal = 0
avdifftotal = int((LASTvalue - FIRSTvalue) /(totalmonths  - 1))
print(f"Average Change: ${avdifftotal}")

#Set File Path
budget_csv_path = os.path.join("Resources", "budget_data.csv")
##print (budget_csv_path)

# Set List

#Scan through list, log prev value, current value and difference. If difference is bigger then last difference  overide current and prev with new values.


Maxvalue = 0
Dateofmax = ""
MaxPH = 0
lastvalue = 0
currentvalue = 0
maxchange = 0

with open(budget_csv_path) as csvfile:
    budgetcsvreader = csv.reader(csvfile, delimiter=",")
    #Skip first line
    next(budgetcsvreader)
    #Search through each row
    for row in budgetcsvreader:
        #see if value is higher than previous value
        lastvalue = currentvalue
        currentvalue = (int(row[1]))
        MaxPH = currentvalue - lastvalue
        if (Maxvalue < MaxPH):
            Dateofmax = (row[0])
            Maxvalue = MaxPH
            lastvalue = (int(row[1]))

print(f"Greatest Increase in Profits: {Dateofmax} (${Maxvalue})")

#Set File Path
budget_csv_path = os.path.join("Resources", "budget_data.csv")
##print (budget_csv_path)

# Set List

#Scan through list, log prev value, current value and difference. If difference is bigger then last difference  overide current and prev with new values.


Minvalue = 0
Dateofmin = ""
MinPH = 0
lastvalue = 0
currentvalue = 0
minchange = 0

with open(budget_csv_path) as csvfile:
    budgetcsvreader = csv.reader(csvfile, delimiter=",")
    #Skip first line
    next(budgetcsvreader)
    #Search through each row
    for row in budgetcsvreader:
        #see if value is higher than previous value
        lastvalue = currentvalue
        currentvalue = (int(row[1]))
        MinPH = currentvalue - lastvalue
        if (Minvalue > MinPH):
            Dateofmin = (row[0])
            Minvalue = MinPH
            lastvalue = (int(row[1]))

print(f"Greatest Decrease in Profits: {Dateofmin} (${Minvalue})")

#Specify the file to write to
output_path = os.path.join("analysis", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline="") as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow([f"Total Months: {totalmonths}"])
    csvwriter.writerow([f"Total: ${pltotal}"])
    csvwriter.writerow([f"Average Change: ${avdifftotal}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {Dateofmax} (${Maxvalue})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {Dateofmin} (${Minvalue})"])



