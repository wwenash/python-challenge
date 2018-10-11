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

#initialize variables 
totalFinal = 0
totalMonths = 0
totalAveChange = 0
index = 0
finalValue = 0
originalValue = 0
maxValue = 0
minValue = 0
maxline = 0
minline = 0

#make Lists
Month = []
MonthlyBalance = []
MonthlyDiff = {}

#define input files and output files
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

# Calculating average change between months
for num , originalValue in enumerate(MonthlyBalance):
   #if original value is not equal to the last element in the List
    if originalValue != int(MonthlyBalance[-1]):

        finalValue = int(MonthlyBalance[num+1])
        monthlydiff = (finalValue - originalValue)
        MonthlyDiff.update({num:monthlydiff})
        totalAveChange = totalAveChange + monthlydiff
        #totalAveChange = totalAveChange + ( finalValue - originalValue )
        index += 1
    else:
        totalAveChange = str(round(totalAveChange / index, 2))

#Calculate the max/min month in the set of 86 months by looking at MonthlyDiff dictonary
maxindex = max(MonthlyDiff, key=MonthlyDiff.get)
maxValue = MonthlyDiff[maxindex]
minindex = min(MonthlyDiff, key=MonthlyDiff.get)
minValue = MonthlyDiff[minindex]

# Print out data of interest...
print(f"\n\nFinancial Analysis\n" + "-" * 25)
print(f"Total Months: {totalMonths}\nGrand Total: ${totalFinal}")
print(f"Average Change: ${totalAveChange}")
print(f"Greatest Increase in Profits: {Month[maxindex+1]} (${maxValue})")
print(f"Greatest Decrease in Profits: {Month[minindex+1]} (${minValue})\n\n")