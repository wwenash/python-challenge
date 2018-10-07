# Homework 03 Python PyBank
# by: 03_Python_PyBank_WEN_WASHSTL201809DATA3

#* Your task is to create a Python script that analyzes the records to calculate each of the following:
#  * The total number of months included in the dataset
#  * The total net amount of "Profit/Losses" over the entire period
#  * The average change in "Profit/Losses" between months over the entire period
#  * The greatest increase in profits (date and amount) over the entire period
#  * The greatest decrease in losses (date and amount) over the entire period
#  * As an example, your analysis should look similar to the one below:
#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# data is located at: ../../WASHSTL201809DATA3/03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv

# import packages
import os
import csv

totalFinal = 0
totalMonths = 0
totalAveChange = 0

Month = []
MonthlyBalance = []

firstPass = False

#define where the data is...
budgetCSV = os.path.join('../../', 'WASHSTL201809DATA3', '03-Python','Homework','Instructions','PyBank','Resources', 'budget_data.csv' )

# open the data... for reading, split on commas, skip header,
# do simple calculations and fill 
with open(budgetCSV, 'r') as budgetFile:

    budgetreader = csv.reader(budgetFile, delimiter=',')
    header = next(budgetreader)

    for row in budgetreader:
        date = row[0]
        Month.append(date)
        
        account = int(row[1])
        MonthlyBalance.append(account)

        totalMonths += 1
        totalFinal = totalFinal + (account)

# Calculating average change
for num in range(0,totalMonths):

    totalAveChange = totalAveChange + (int(MonthlyBalance[num]) - int(MonthlyBalance[num - 1]))



# Print out data of interest...
print(f"\n\nTotal Months: {totalMonths}")
print(f"Grand Total: ${totalFinal}")

print(f"\n\nTotal Change: ${totalAveChange}")


