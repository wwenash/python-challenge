# Homework 03 Python PyPoll
# by: 03_Python_PyPoll_WEN_WASHSTL201809DATA3

#* The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.
#* As an example, your analysis should look similar to the one below:

#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#  ```
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# import packages
import os
import csv

# initialize variables
voterCount = 0

# make Lists/Dictionaries
Election = {}
ElectionVoter =[]

county = set()
canidate = set()

myvotes = {}

# define input and output files
#electionCSV = os.path.join('../../', 'WASHSTL201809DATA3','03-Python','Homework','Instructions','PyPoll','Resources', 'election_data.csv')
testElectionCSV = os.path.join('../../', 'WASHSTL201809DATA3','03-Python','Homework','Instructions','PyPoll','Resources', 'TEST_election_data.csv')

with open(testElectionCSV, 'r') as electionFile:

    resultsreader = csv.reader(electionFile, delimiter=',')
    header = next(resultsreader)

    for line in resultsreader:
        #print(line)
        Election[line[0]] = line[1:]

#print(f"{Election.keys()}")
for keys in Election.keys():
    ElectionVoter.append(keys)
    voterCount += 1

#print(f"{voterCount}")
for key, value in Election.items():
    county.add(value[0])
    canidate.add(value[1])
    #print(f"{value[1]}")

    if str(value[1]) not in myvotes.items():
        #myvotes.update({value[1]:1})
        person = str(value[1])
        myvotes.update({'person':1})
        #print(f"{myvotes.keys()}")

    elif str(value[1]) in myvotes.keys():
        myvotes[1] += 1
 
print(f"\nHello\n {myvotes.keys()}")

